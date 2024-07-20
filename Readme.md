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

