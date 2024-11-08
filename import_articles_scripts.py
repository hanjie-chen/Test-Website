# from app import app
import os
import frontmatter
import re
from models import Article_Meta_Data
from datetime import date
from flask_sqlalchemy import SQLAlchemy


def import_articles(db: SQLAlchemy, Articles_Directory: str):
    # 获取所有.md files
    md_files = [f for f in os.listdir(Articles_Directory) if f.endswith('.md')]

    for md_file in md_files:
        md_path = os.path.join(Articles_Directory, md_file)
        with open(md_path, 'r', encoding='utf-8') as f:
            article = f.read()
        
        # article = metadata + body
        # the article without <!-- split --> means not ready to published
        # only split once, which means when it met first <!-- split -->, it split and then stop
        split = article.split('<!-- split -->', 1)
        if len(split) != 2:
            print(f"file: {md_file} lack <!-- split -->, not ready to be published, jumped")
            continue
        
        metadata_part = split[0]
        body_part = split[1]

        # use body_part to generate html file

        # extra metadata 
        post = frontmatter.loads(metadata_part)
        metadata = post.metadata
        left_content = post.content

        # extra BriefIntroduction, this part wrapped by ```
        brief_intro_pattern = re.compile(r'```.*?BriefIntroduction:\s*(.*?)```', re.DOTALL)
        brief_intro_match = brief_intro_pattern.search(left_content)
        if brief_intro_match:
            brief_intro_text = brief_intro_match.group(1).strip()
        else:
            brief_intro_text = ''
            print(f"文件 {md_file} 的 BriefIntroduction 部分解析失败。")
        
        # extra file last modified time
        # only consider modified_time to auto generate, beucase the create time will be chagned if file moved between different OS
        file_stat = os.stat(md_path)
        file_last_modfiled_time = date.fromtimestamp(file_stat.st_mtime)

        # create database modles instance
        article_metadata = Article_Meta_Data(
            title = metadata.get('Title', 'Untitled'),
            author = metadata.get('Author', 'Plain'),
            instructor = metadata.get('Instructor'),
            cover_image_url = metadata.get('CoverImage','unknow'),
            # if none use today
            rollout_date = metadata.get('RolloutDate', date.today()),
            category = metadata.get('Category', 'uncalssified'),
            ultimate_modified_date = file_last_modfiled_time,
            brief_introduction = brief_intro_text
        )

        # check if there are same title articles
        # exist_check = Article_Meta_Data.query.filter_by(title = article_metadata.title).first()
        exist_check = db.session.execute(
            db.select(Article_Meta_Data)
            .where(Article_Meta_Data.title == article_metadata.title)
            ).scalar()
        # consider realize a git-like system to track the new file and chagned file, only 
        if exist_check:
            print(f'Article {article_metadata.title} exists in database, please check again, skipped')
            continue
        
        db.session.add(article_metadata)
        print(f'Article {article_metadata.title} added')

    db.session.commit()
    print("All articles have been imported.")

