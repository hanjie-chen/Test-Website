from app import app
import os

Articles_Directory = "/home/Plain/Personal_Project/Test_Articles_Data"

def import_articles():
    # 获取所有.md files
    md_files = [f for f in os.listdir(Articles_Directory) if f.endswith('.md')]

    for md_files in md_files:
        pass