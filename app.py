from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # use the file in the templates
    return render_template("hello_world.html")

# deal with 404 error
@app.errorhandler(404)
def page_not_found(error_info):  # 接受异常对象作为参数
    print(f"Error: {error_info}, Description: {error_info.description}, URL: {request.url}") # 打印错误信息到控制台
    return render_template('404.html', error = error_info, url = request.url), 404  # 将错误信息传递给模板
