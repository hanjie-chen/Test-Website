from app import app
import os
import frontmatter
import re
from models import db, Article_Meta_Data
from datetime import date
from sqlalchemy import select

Articles_Directory = "/home/Plain/Personal_Project/Test_Articles_Data"

def import_articles():
    # 获取所有.md files
    md_files = [f for f in os.listdir(Articles_Directory) if f.endswith('.md')]

    for md_file in md_files:
        md_path = os.path.join(Articles_Directory, md_file)
        with open(md_path, 'r', encoding='utf-8') as f:
            article = f.read()
        
        # article = metadata + body
        split = article.split('<!-- split -->', 1)
        if len(split) != 2:
            print(f"file: {md_file} lack <!-- split -->, jumped")
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
        file_stat = os.stat(md_file)
        file_last_modfiled_time = date.fromtimestamp(file_stat.st_mtime)

        # 创建数据库实例
        article_metadata = Article_Meta_Data(
            title = metadata.get('Title', 'Untitled'),
            author = metadata.get('Author', 'Plain'),
            instructor = metadata.get('Instructor'),
            cover_image_url = metadata.get('CoverImage','unknow'),
            rollout_date = date.fromisoformat(metadata.get('RolloutDate')),
            category = metadata.get('Category', 'uncalssified'),
            ultimate_modified_date = file_last_modfiled_time,
            brief_introduction = brief_intro_text
        )

        # check if there are same title articles
        # exist_check = Article_Meta_Data.query.filter_by(title = article_metadata.title).first()
        exist_check = db.session.scalar(select(Article_Meta_Data).where(Article_Meta_Data.title == article_metadata.title))
        exist_check = db.session.execute(db.select)
        if exist_check:
            print(f'Article {article_metadata.title} exists, please check again, skipped')
            continue

        db.session.add(article_metadata)
        print(f'Article {article_metadata.title} added')

    db.session.commit()
    print("All articles have been imported.")
