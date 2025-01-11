import os
import re
import frontmatter
import shutil
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from config import Rendered_Articles
from models import Article_Meta_Data
from markdown_render_scripts import render_markdown_to_html

# future considered: use pathlib.Path instead of os.path
# consider use python logging package to instead of print information

# regular expression pre-compile
brief_intro_pattern = re.compile(r'```.*?BriefIntroduction:\s*(.*?)```', re.DOTALL)

def divide_files_and_folders(path: str):
    """
    return the files and folders in a directory
    """
    all_items = os.listdir(path)
    # ignore the folder named "__<foldername>__" and ".<foldername>"
    files_and_folders = [item for item in all_items if not (
        (item.startswith('__') and item.endswith('__')) or 
        item.startswith('.')
                        )]
    files = [file for file in files_and_folders if os.path.isfile(os.path.join(path, file))]
    folders = [folder for folder in files_and_folders if os.path.isdir(os.path.join(path, folder))]
    return files, folders

def get_dst_path(current_dir: str, root_dir: str):
    """ get the path of rendered file  """
    relative_path = os.path.relpath(current_dir, root_dir)
    destination_path = os.path.join(Rendered_Articles, relative_path.replace(os.sep, '-'))
    return destination_path

def validate_and_extract(md_path: str):
    """
    validate a md file whether read to lanch on the webiste
    extract ymal-metadata, brief introduction, content_part which need to render
    if validate pass, return brief_intro_text, metadata, content_part
    if validate failed, return False
    """

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            single_article = f.read()
    except Exception as e:
        print(f"Error reading file {md_path}: {e}. Skipped.")
        return False
    
    # single article = metadata part + content part
    # only divide once, which means when it met first <!-- split -->, it will divide and stop
    divided_article = single_article.split('<!-- split -->', 1)
    if len(divided_article) != 2:
        print(f"file: {md_path} lacks <!-- split -->, not ready to be published, skipped")
        return False
    
    metadata_part = divided_article[0]
    content_part = divided_article[1]

    # extra real metadata and brief introduction
    post = frontmatter.loads(metadata_part)
    real_metadata = post.metadata
    brief_intro = post.content

    # extra brief introduction
    brief_intro_match = brief_intro_pattern.search(brief_intro)
    if not brief_intro_match:
        print(f"file {md_path} lack brief introduciton, not ready to published, skipped")
        return False
    brief_intro_text = brief_intro_match.group(1).strip()

    # validate metadata field, empty not allowed
    # Instructor can be empty
    required_fields = ["Title", "Author", "CoverImage", "RolloutDate"]
    for field in required_fields:
        if not real_metadata.get(field):
            print(f"file {md_path} metadata {field} is empty, not ready to published, skipped")
            return False
    
    return brief_intro_text, real_metadata, content_part

def process_article(md_filename: str, current_dir: str, root_dir: str, db: SQLAlchemy):
    """deal with single .md file"""

    # the path store the rendered file
    output_path = get_dst_path(current_dir, root_dir)

    md_path = os.path.join(current_dir, md_filename)
    
    result = validate_and_extract(md_path)
    if not result:
        return
    brief_intro_text, metadata, content_part = result
    print(f"file {md_path} pass validate, ready to launch")

    # extra file last modified time
    # only consider modified_time to auto generate, beucase the create time will be chagned if file moved between different OS
    file_stat = os.stat(md_path)
    file_last_modified_time = date.fromtimestamp(file_stat.st_mtime)

    # get category | get relative path
    rel_path = os.path.relpath(md_path, root_dir)
    article_category = os.path.split(rel_path)[0]

    # generate true cover_image_url
    raw_image_path = metadata.get('CoverImage')
    cover_image_path = os.path.join(output_path, raw_image_path.lstrip("./"))

    # create database models instance
    # if Instructor is empty, default set to nobody
    article_metadata = Article_Meta_Data(
        title=metadata.get('Title'),
        author=metadata.get('Author'),
        instructor=metadata.get('Instructor', 'nobody'),
        rollout_date=metadata.get('RolloutDate'),
        cover_image_url=cover_image_path,
        category=article_category,
        ultimate_modified_date=file_last_modified_time,
        brief_introduction=brief_intro_text
    )

    # check if there are same title articles
    exist_check = db.session.execute(
        db.select(Article_Meta_Data)
        .where(
            Article_Meta_Data.title == article_metadata.title,
            Article_Meta_Data.category == article_metadata.category
        )
    ).scalar()

    if exist_check:
        print(f'Article {article_metadata.title} exists in database, skipped')
        return
    
    db.session.add(article_metadata)
    # flush() to get the database primary key
    db.session.flush()
    print(f'Article {article_metadata.category}/{article_metadata.title} added')

    html_filename = article_metadata.id
    render_markdown_to_html(content_part, html_filename, output_path)

def import_articles(root_dir: str, db: SQLAlchemy):
    """
    scan articles directory and copy images file
    and rendered md file to html file
    """

    def _recursive_scan(current_dir: str):
        """
        recursive articles data directory
        copy the images/assets folder and rendered md file to html
        """

        # get files and folders in current dir
        files, folders = divide_files_and_folders(current_dir)

         # if images/assets folder exists which means it reach articles md file
        if 'images' in folders:
            exist_folder = 'images'
        elif 'assets' in folders:
            exist_folder = 'assets'
        else:
            exist_folder = None

        if exist_folder:
            # get destination path
            destination_path = get_dst_path(current_dir, root_dir)
            
            # create destination folder
            os.makedirs(destination_path)

            # copy images from source to destination
            source_images_path = os.path.join(current_dir, exist_folder)
            destination_images_path = os.path.join(destination_path, exist_folder)
            shutil.copytree(source_images_path, destination_images_path)
            print(f"copy images from {source_images_path} to {destination_images_path} successfully")

            # if exist then its articles folder | deal with all md file
            for file in files:
                if file.endswith('.md'):
                    process_article(file, current_dir, root_dir, db)
        else:
            # if not exist go deeper dir
            for folder in folders:
                sub_dir_path = os.path.join(current_dir, folder)
                _recursive_scan(sub_dir_path)

    # if rednered-articles folder/file exists before, delete it
    if os.path.exists(Rendered_Articles):
        if os.path.isdir(Rendered_Articles):
            shutil.rmtree(Rendered_Articles)
        else:
            os.remove(Rendered_Articles)
    # recursive articles directory and rendered it
    _recursive_scan(root_dir)
    db.session.commit()
    print("All articles have been imported.")