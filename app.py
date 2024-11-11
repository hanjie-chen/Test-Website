from flask import Flask, render_template, request, send_from_directory
from models import db, Article_Meta_Data
from import_articles_scripts import import_articles

app = Flask(__name__)

# configure the database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
# use memory as test
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# articles directory
Articles_Directory = "/home/Plain/Personal_Project/Test_Articles_Data"
# rendered articles directory(which is html)
Rendered_Articles = "./rendered_articles/"

# register teh rendered_articles as static folder
app.add_url_rule(Rendered_Articles, endpoint="Articles", view_func=lambda filename: send_from_directory(Rendered_Articles, filename))

# 初始化应用
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    import_articles(db, Articles_Directory)

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

@app.route("/Articles/<title>")
def view_articles(title):
    article = db.session.execute(
        db.select(Article_Meta_Data)
        .where(Article_Meta_Data.title == title)
    ).scalar()

    if not article:
        return "Artilces not found", 404
    # wait for complised
    return render_template()