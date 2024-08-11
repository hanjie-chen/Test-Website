# About the website

This is the Frontend website of my personal website. Lask time I try to develop frontend and backend in both, but actaully failed because I stuck in the backend database desing and deploy.



# About the requirements.txt

1. how the content be generated?

about the content in the `requirements.txt`, I generate by the command `pip3 freeze > requirements.txt`

2. how to use the file

use the command `pip install -r requirements.txt` to install the dependency of the requirements.



# About the website icon design

[Yesicon - 精选全球高品质、开源、免费的矢量图标库](https://yesicon.app/?lang=zh-hans)

use that website to get icon



# LLM Prompt

我在搭建一个个人网站，使用python flask框架，前端采用Bootstrap5，目前正在搭建前端部分。这是我目前的项目目录结构

```powershell
├─static
│  ├─bootstrap5
│  │  ├─css
│  │  └─js
│  ├─font
│  │  ├─JetBrainsMono
│  │  └─PingFangSC
│  ├─icon
│  └─images
│      └─headavatar
├─templates
└─__pycache__

and the file in the templates
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         8/11/2024   4:27 PM            319 404.html
-a----         8/11/2024   4:32 PM            171 about_me.html
-a----         8/11/2024   4:31 PM            174 article_index.html
-a----         7/24/2024  12:27 AM            288 hello_world.html
-a----         8/11/2024   4:36 PM           3457 index.html
-a----         8/11/2024   4:21 PM           4127 TemplatesOverview.md
```
这是我现在正在编写index.html界面
```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plain Personal Website</title>
    <!-- 网站图标 -->
    <link rel="icon" href="/static/icon/favicon_point.ico" type="image/x-icon">


    <!-- Bootstrap 5 CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap5/css/bootstrap.min.css') }}">
    <!-- use the pointed font -->
    <link rel="stylesheet" href="{{ url_for('static', filename='font/font.css') }}">
    <!-- pointed body color -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css')}}">
   
</head>
<body>
  <main class="d-flex flex-column min-vh-100">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-sm navbar-custom fixed-top">
      <div class="container">
        <!-- put my personal website logo here -->
        <!-- <a class="navbar-brand" href="{{ url_for('index')}}">
          <img alt="头像" class="rounded" style="width:4vw;" src="{{ url_for('static', filename='images/headavatar/head_avatar_problem.png') }}">
        </a> -->
        <span>
          Welcome to my personal website
        </span>
        <div class="collapse navbar-collapse" id="mynavbar">
          <ul class="navbar-nav ms-auto">
            <!-- 文章页面就可以包含分类和标签了 不用另外起一个页面 -->
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('article_index') }}">
                 Article
              </a>
            </li>
            <li class="nav-item">
              <span class="nav-link">|</span>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('about_me') }}">
                 About Me
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    

    <!-- Main Content -->
    <div class="main-content container-fluid flex-grow-1 d-flex align-items-center justify-content-center">
      <div class="content-wrapper">
        <div class="container text-center mb-4">
          <img alt="avatar" class="rounded" style="width: 8vw;" src="{{ url_for('static', filename='images/headavatar/head_avatar_problem.png') }}">
        </div>
        <div class="content">
          <h5 class="mb-3">👋 hi, 我是翰杰, earth online的一名NPC</h5>
          <h5 class="mb-3">🎓 我是一名 emm…… 原神玩家（好吧，这么说是因为我不知道应该说什么）</h5>
          <h5 class="mb-3">💻 我正在使用 Python Flask 和 Bootstrap 5 构建个人网站前端部分</h5>
          <h5 class="mb-3">🌟 我对二次元充满热情，省流，宅男</h5>
          <h5 class="mb-3">🚀 我的长期目标是不工作，每天可以自由的支配时间，尝试自己感兴趣的事情</h5>
          <h5 class="mb-3">📫 联系我：<a href="mailto:hanjiechen@outlook.com">hanjie-chen@outlook.com</a></h5>
        </div>
      </div> 
    </div>

    <!-- Footer -->
    <footer class="footer-custom py-3 ">
      <div class="container text-center">
        <span>&copy; 2024 for Plain Personal Website</span>
      </div>
    </footer>
        
  </main>
  <!-- Bootstrap 5 JS Bundle with Popper -->
  <script src="{{ url_for('static', filename='bootstrap5/js/bootstrap.bundle.min.js') }}"></script>
</body>
</html>


```
这是我写的main.py
```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # use the file in the templates
    return render_template("index.html")

# deal with 404 error
@app.errorhandler(404)
def page_not_found(error_info):  # 接受异常对象作为参数
    # print(f"Error: {error_info}, Description: {error_info.description}, URL: {request.url}") # 打印错误信息到控制台
    return render_template('404.html', error = error_info, url = request.url), 404  # 将错误信息传递给模板

```

但是我发现每当我运行
