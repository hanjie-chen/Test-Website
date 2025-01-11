# About the website

This is the Frontend website of my personal website. Lask time I try to develop frontend and backend in both, but actaully failed because I stuck in the backend database desing and deploy.

Now I trying to develop the backend part of my website, I'd to choose the SQLite as my database to store my articles.

# future consider

[waf](https://github.com/chaitin/SafeLine)

# LLM Prompt

## Backend

我正在搭建一个个人网站，使用python Flask框架，CSS采用Bootstrap5，数据库采用SQLite，并且使用SQLAlchemy和Flask-SQLAlchemy扩展来访问SQLite数据库。我打算将网站部署到一块树莓派4B上面。

我打算使用这个网站发布一些自己写的文章，包括技术类的，还有生活类的，还有自己的思考，文章使用markdown及其扩展语法。我打算将文章的元数据包括文章标题，文章封面图片链接，文章最后修改日期，文章作者，文章指导者，文章分类，文章简介，存储在sqlite数据库，文章本体则使用markdown编辑器来编辑，一篇文章一个文件夹，其中包含文章和图片文件夹。

网站目前只包含2个部分，首页和文章分类页面。其中首页主要是简单的自我介绍和本网站介绍。文章分类页面包含了文章的分类，以及各个分类之下的文章元数据卡片。我打算使用嵌套集合模型 [Nested Set Model] 来实现文章分类的树形结构

请你在接下来的对话中牢记这些信息。如果你已经记住，请你只回答“明白”

## next action

artilces meta date 加上一条rendered html file name, 用来定位html的位置

在路由函数中直接从数据库中拿去rendered html file name

在rendered_artilces 文件夹中平铺所有的文件，不需要创建文件夹的树形结构，方便路由函数拿取文件

## docker part
我正在使用python flask 写一个web app作为我的个人博客网站，在这个过程中尽可能多的学习知识。

这是我的项目目录

```
Plain@Linux-VM:~/Personal_Project/test-website$ tree -L 2
.
├── Readme.md
├── articles-data
│   ├── Dockerfile
│   ├── init.sh
│   ├── logrotate.conf
│   └── update-articles.sh
├── compose.yml
└── web-app
    ├── Dockerfile
    ├── __pycache__
    ├── app.py
    ├── config.py
    ├── import_articles_scripts.py
    ├── instance
    ├── markdown_render_scripts.py
    ├── models.py
    ├── rendered_articles
    ├── requirements.in
    ├── requirements.txt
    ├── static
    └── templates

7 directories, 14 files
```

这是我的 compose.yml

```
services:
  web-app:
    build:
      context: ./web-app
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    volumes:
      - articles_data:/articles-data:ro
    environment:
      - ARTICLES_DIRECTORY=/articles-data
      - FLASK_APP=app.py
    develop:
      watch:
        - path: ./web-app
          target: /app
          action: sync+restart

  articles-data:
    build:
      context: ./articles-data
      dockerfile: Dockerfile
    volumes:
      - articles_data:/articles-data:rw
    environment:
      - GITHUB_REPO=https://github.com/hanjie-chen/PersonalArticles.git
      - REPO_BRANCH=main
      - LOG_DIR=/var/log/personal-website
    develop:
      watch:
        - path: ./articles-data
          action: restart

volumes:
  articles_data:
```

这是我的web-app/Dockerfile

```
# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# set web app directory
WORKDIR /app

# 复制requirements.txt
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

COPY . .

# 暴露端口（Flask默认使用5000端口）
EXPOSE 5000

# 启动命令
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
```

这是articles-data

```
FROM alpine:3.19

# install git and dcron
RUN apk add --no-cache git dcron logrotate

# create log directory and log file, set the log file permission
RUN mkdir -p /var/log/personal-website && \
    touch /var/log/personal-website/{articles-sync,crond}.log &&\
    chmod 644 /var/log/personal-website/*.log

# create logrotate dir and copy file
COPY logrotate.conf /etc/logrotate.d/personal-website

WORKDIR /articles-data

# copy the scripts, provide the permission, and set cron jobs
COPY update-articles.sh init.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/update-articles.sh && \
    chmod +x /usr/local/bin/init.sh

ENTRYPOINT [ "/usr/local/bin/init.sh" ]
```





