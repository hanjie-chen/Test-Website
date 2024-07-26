# About the website

This is the Frontend website of my personal website. Lask time I try to develop frontend and backend in both, but actaully failed because I stuck in the backend database desing and deploy.



# About the requirements.txt

1. how the content be generated?

about the content in the `requirements.txt`, I generate by the command `pip3 freeze > requirements.txt`

2. how to use the file

use the command `pip install -r requirements.txt` to install the dependency of the requirements.



# LLM Prompt

我在搭建一个个人网站，使用python flask框架，前端采用Bootstrap5，目前正在搭建前端部分。这是我目前的项目目录结构

```powershell
E:.
│  .gitignore
│  app.py
│  Readme.md
│  requirements.txt
│
├─static
│  │  StaticOverivew.md
│  │  style.css
│  │
│  ├─bootstrap5
│  │  ├─css
│  │  │      bootstrap-grid.css
│  │  │      bootstrap-grid.css.map
│  │  │      bootstrap-grid.min.css
│  │  │      bootstrap-grid.min.css.map
│  │  │      bootstrap-grid.rtl.css
│  │  │      bootstrap-grid.rtl.css.map
│  │  │      bootstrap-grid.rtl.min.css
│  │  │      bootstrap-grid.rtl.min.css.map
│  │  │      bootstrap-reboot.css
│  │  │      bootstrap-reboot.css.map
│  │  │      bootstrap-reboot.min.css
│  │  │      bootstrap-reboot.min.css.map
│  │  │      bootstrap-reboot.rtl.css
│  │  │      bootstrap-reboot.rtl.css.map
│  │  │      bootstrap-reboot.rtl.min.css
│  │  │      bootstrap-reboot.rtl.min.css.map
│  │  │      bootstrap-utilities.css
│  │  │      bootstrap-utilities.css.map
│  │  │      bootstrap-utilities.min.css
│  │  │      bootstrap-utilities.min.css.map
│  │  │      bootstrap-utilities.rtl.css
│  │  │      bootstrap-utilities.rtl.css.map
│  │  │      bootstrap-utilities.rtl.min.css
│  │  │      bootstrap-utilities.rtl.min.css.map
│  │  │      bootstrap.css
│  │  │      bootstrap.css.map
│  │  │      bootstrap.min.css
│  │  │      bootstrap.min.css.map
│  │  │      bootstrap.rtl.css
│  │  │      bootstrap.rtl.css.map
│  │  │      bootstrap.rtl.min.css
│  │  │      bootstrap.rtl.min.css.map
│  │  │
│  │  └─js
│  │          bootstrap.bundle.js
│  │          bootstrap.bundle.js.map
│  │          bootstrap.bundle.min.js
│  │          bootstrap.bundle.min.js.map
│  │          bootstrap.esm.js
│  │          bootstrap.esm.js.map
│  │          bootstrap.esm.min.js
│  │          bootstrap.esm.min.js.map
│  │          bootstrap.js
│  │          bootstrap.js.map
│  │          bootstrap.min.js
│  │          bootstrap.min.js.map
│  │
│  ├─font
│  │  │  font.css
│  │  │
│  │  ├─JetBrainsMono
│  │  │      JetBrainsMono-Regular.ttf
│  │  │      JetBrainsMono-Regular.woff2
│  │  │
│  │  └─PingFangSC
│  │          PingFangSCRegular.ttf
│  │          PingFangSCRegular.woff2
│  │
│  ├─icon
│  │      favicon_point.ico
│  │      favicon_wind.ico
│  │
│  └─images
│      │  paimon.gif
│      │  shogun.gif
│      │
│      └─headavatar
│              head_avatar_oh.png
│              head_avatar_problem.png
│              head_avatar_think.png
│
└─templates
        404.html
        hello_world.html
        index.html
        TemplatesOverview.md
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
  <main>
    <nav class="navbar navbar-expand-sm navbar-custom fixed-top">
      <!-- test -->
    </nav>
    
    
    <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center p-5">
          <div class="content-wrapper">
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

    <footer>
      <!-- <div class="text-center">
        <small>&copy; 2024 for Plain Personal Website</small>
      </div> -->
    </footer>  
        
  </main>
 
  <!-- Bootstrap 5 JS Bundle with Popper -->
  <script src="{{ url_for('static', filename='bootstrap5/js/bootstrap.bundle.min.js') }}"></script>
</body>
</html>


```
我想要添加一个nav bar和footer,但是想要的效果是在一整个屏幕显示，如下
