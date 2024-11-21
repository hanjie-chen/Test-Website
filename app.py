from flask import Flask, render_template, request, send_from_directory, abort
from models import db, Article_Meta_Data
from import_articles_scripts import import_articles
import os

app = Flask(__name__)

# configure the database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# use memory as test
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# articles directory
Articles_Directory = "/home/Plain/Personal_Project/articles-data-test"
# Rendered articles directory (relative to project root)
Rendered_Articles = "rendered_articles"

# Configure static folders
app.static_folder = 'static'  # default static folder for CSS, JS, etc.
# Register rendered_articles as additional static folder
app.config['RENDERED_ARTICLES_FOLDER'] = os.path.join(app.root_path, Rendered_Articles)
# 注册rendered_articles为静态文件夹
app.add_url_rule('/rendered_articles/<path:filename>',
                 endpoint='rendered_articles',
                 view_func=lambda filename: send_from_directory(app.config['RENDERED_ARTICLES_FOLDER'], filename))

# 初始化应用
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    import_articles(Articles_Directory, db)

@app.route("/")
def index():
    # use the file in the templates
    return render_template("index.html")

@app.route("/Articles")
def article_index():
    # 从数据库中获取所有文章
    articles = db.session.execute(db.select(Article_Meta_Data)).scalars().all()
    return render_template("article_index.html", articles=articles)


@app.route("/AboutMe")
def about_me():
    return render_template("about_me.html")

# deal with 404 error
@app.errorhandler(404)
def page_not_found(error_info):  # 接受异常对象作为参数
    # print(f"Error: {error_info}, Description: {error_info.description}, URL: {request.url}") # 打印错误信息到控制台
    return render_template('404.html', error = error_info, url = request.url), 404  # 将错误信息传递给模板

@app.route("/Articles/<int:article_id>")
def view_article(article_id):
    article = db.session.execute(
        db.select(Article_Meta_Data)
        .where(Article_Meta_Data.id == article_id)
    ).scalar()

    if not article:
        abort(404)
    
    # 转换category中的/为-以匹配文件系统路径
    category_path = article.category.replace('/', '-')
    
    # 构建相对于/rendered_articles的路径
    html_filename = f"{article_id}.html"
    relative_path = f"{category_path}/{html_filename}"
    
    # 检查文件是否存在
    if not os.path.exists(os.path.join(app.config['RENDERED_ARTICLES_FOLDER'], category_path, html_filename)):
        abort(404)
    
    # 返回模板，使用相对路径
    return render_template('article_details.html', 
                         article=article,
                         article_content_path=f"/rendered_articles/{relative_path}")


# 在路由函数之前添加这些调试代码
@app.route("/debug")
def debug_info():
    # 1. 检查数据库中的文章
    articles = db.session.execute(db.select(Article_Meta_Data)).scalars().all()
    db_info = "Database Articles:\n"
    for article in articles:
        db_info += f"ID: {article.id}, Title: {article.title}, Category: {article.category}\n"
    
    # 2. 检查rendered_articles目录
    rendered_path = app.config['RENDERED_ARTICLES_FOLDER']
    dir_info = f"\nRendered Articles Directory ({rendered_path}):\n"
    if os.path.exists(rendered_path):
        for root, dirs, files in os.walk(rendered_path):
            dir_info += f"Directory: {root}\n"
            for file in files:
                dir_info += f"  File: {file}\n"
    else:
        dir_info += "Directory does not exist!\n"
    
    # 3. 显示应用
    config_info = "\nApp Configuration:\n"
    config_info += f"RENDERED_ARTICLES_FOLDER: {app.config['RENDERED_ARTICLES_FOLDER']}\n"
    
    return f"<pre>{db_info}\n{dir_info}\n{config_info}</pre>"
