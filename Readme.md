# About the website

## articles-sync container
articles-sync container 用于管理我的 markdown 笔记文章, 使用 alpine:3.19 作为image
因为我的笔记文章存放在一个 github repository 中，并且常常更新，所以它的主要作用是每天定期的 git pull 这个 github repository 到某一个目录中，而这个目录实际上是一个 docker volumes 挂载上去的，它对这个目录有读写的权限
我使用 crond 定期执行一个 shell 脚本来实现定期 git pull, 并且将 cornd 执行日志， shell 脚本执行日志使用了 logrotate 防止它过大

## web-app container
web-app container 作为我的网站主体，使用 python flask 3.x 开发, 使用 python:3.9 slim 作为image
它同样挂载 docker volumes, 但是对其只有读的权限，他会去这个目录下拿取我的 markdown 文章
首先提取 metadata 插入数据库，然后处理文章的内容，我使用 python-markdown 将其渲染为 html 并且存放在 rendered-articles 目录下
并将这个目录注册为一个staic folder, 这样子 flask 路由函数就可以找到这些 html
为了实现一些特殊的 markdown 渲染效果，我自己写了一些 python-markdown extension, 比如说客制化的 GFM-admonition 等

### rendered-articles design
我原本的 markdown 笔记结构如下所示
```
└───python-learn
    ├───python-language
    │   ├───Python_Basic
    │   └───Python_Philosophy
    ├───python-package
    │   ├───Flask
    │   │   └───images
    │   ├───flask-sqlalchemy
    │   │   └───images
    │   ├───frontmatter+yaml
    │   ├───SQLAlchemy
    │   │   └───images
    │   └───standard-library
    │       ├───re
    │       │   └───images
    │       └───shutil
    └───python-practices
```
是多层的树形结构，但是这是为了方便我写文章和分类，但对我的网站来说则不需要多层的树形结构，所以我使用 `-` 代替了路径中的 `/` 将其存放于 rendered-articles 目录下面
```
rendered-articles/
├── PythonLearn-PythonPackage-SQLAlchemy
│   ├── 2.html
│   └── images
│       └── cover_image.png
├── PythonLearn-PythonPackage-flask-sqlalchemy
│   ├── 3.html
│   └── images
│       └── cover_image.webp
└── ToolGuide-GitGuide
    ├── 1.html
    └── images
        └── cover_image.png
```
最多只有2层目录

### database design

为了管理的文章元数据，我针对 category 和 coverimage url 设计如下
```   
   
# 文章封面链接 真实image存储地址 由于特别设计，所以可以由category+相对路径转换而来
# 例如 PythonLearn/PythonPackage/Flask/images/cover-image.png 其 cover_image_url = "redered-articles/PythonLearn-PythonPackage-Flask/images/cover-image.png"
cover_image_url: Mapped[str] = mapped_column(String(100))

# 文章分类 是文章的路径
# 例如 PersonalActicles/PythonLearn/PythonPackage/Flask/Basic.md 其 category = "PythonLearn/PythonPackage/Flask"
# 暂时定义最大长度 1024 个字符
category: Mapped[str] = mapped_column(String(1024))
```


# future consider

1/ add nginx container as reverse proxy
2/ try to use bootstrap5 to opt the css effect
3/ connect to sqlite database to show the data in the sqlite
4/ consider intergate the logs in platform







# website design

consider:

[Windows | Oh My Posh](https://ohmyposh.dev/docs/installation/windows#update)

