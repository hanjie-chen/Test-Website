import os
import re
import frontmatter
import shutil
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from models import Article_Meta_Data
from markdown_render_scripts import render_markdown_to_html

# future considered: use pathlib.Path instead of os.path

def get_dst_path(current_dir: str, root_dir: str):
    """ get the path of rendered file  """
    relative_path = os.path.relpath(current_dir, root_dir)
    destination_path = os.path.join('rendered_articles', relative_path.replace(os.sep, '-'))
    return destination_path

def import_articles(root_dir: str, db: SQLAlchemy):
    """scan articles directory and copy images file"""

    def _recursive_scan(current_dir: str):
        # if images folder exists which means it reach articles md file
        if 'images' in os.listdir(current_dir):
            # get destination path
            destination_path = get_dst_path(current_dir, root_dir)

            #  if destination path exist, delete it
            if os.path.exists(destination_path):
                shutil.rmtree(destination_path)
            
            # create destination folder
            os.makedirs(destination_path)

            # copy images from source to destination
            source_images_path = os.path.join(current_dir, 'images')
            destiantion_images_path = os.path.join(destination_path, 'images')
            shutil.copytree(source_images_path, destiantion_images_path)
            print(f"copy images from {source_images_path} to {destiantion_images_path} successed")

            # if exist then its articles folder | deal with all md file
            for file in os.listdir(current_dir):
                if file.endswith('.md'):
                    process_article(file, current_dir, root_dir, db)
        else:
            # if not exist go deeper dir
            for sub_dir in os.listdir(current_dir):
                sub_dir_path = os.path.join(current_dir, sub_dir)
                if os.path.isdir(sub_dir_path):
                    _recursive_scan(sub_dir_path)

    _recursive_scan(root_dir)
    db.session.commit()
    print("All articles have been imported.")

def process_article(md_filename: str, current_dir: str, root_dir: str, db: SQLAlchemy):
    """deal with single .md file"""

    md_path = os.path.join(current_dir, md_filename)
    with open(md_path, 'r', encoding='utf-8') as f:
        article = f.read()
    
    # article = metadata + body
    # the article without <!-- split --> means not ready to published
    # only split once, which means when it met first <!-- split -->, it split and then stop
    split = article.split('<!-- split -->', 1)
    if len(split) != 2:
        print(f"file: {md_path} lack <!-- split -->, not ready to be published, jumped")
        return
    
    metadata_part = split[0]
    # use body part to generate the html file
    body_part = split[1]

    # extra metadate
    post = frontmatter.loads(metadata_part)
    metadata = post.metadata
    left_content = post.content

    # extra brief introduction
    brief_intro_pattern = re.compile(r'```.*?BriefIntroduction:\s*(.*?)```', re.DOTALL)
    brief_intro_match = brief_intro_pattern.search(left_content)
    if brief_intro_match:
        brief_intro_text = brief_intro_match.group(1).strip()
    else:
        brief_intro_text = ''
        print(f"brief-introduction parse failed file {md_path} ")

    # extra file last modified time
    # only consider modified_time to auto generate, beucase the create time will be chagned if file moved between different OS
    file_stat = os.stat(md_path)
    file_last_modified_time = date.fromtimestamp(file_stat.st_mtime)

    # get category | get relative path
    rel_path = os.path.relpath(md_path, root_dir)
    article_category = os.path.split(rel_path)[0]

    # create database models instance
    article_metadata = Article_Meta_Data(
        title=metadata.get('Title', 'Untitled'),
        author=metadata.get('Author', 'Plain'),
        instructor=metadata.get('Instructor'),
        cover_image_url=metadata.get('CoverImage', 'unknown'),
        rollout_date=metadata.get('RolloutDate', date.today()),
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
    # to get the database primary key
    db.session.flush()
    print(f'Article {article_metadata.title} added')

    html_filename = article_metadata.id
    render_markdown_to_html(body_part, html_filename, get_dst_path(current_dir, root_dir))
