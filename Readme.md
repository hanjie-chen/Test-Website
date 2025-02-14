# About the website

## articles-sync container
这个 container 用于管理我的 markdown 笔记文章, 我的笔记文章存放在一个 github repository 中，并且常常更新
它的主要作用是每天定期的 git pull 这个 repos 到某一个目录中，而这个目录实际上是一个 docker volumes 挂载上去的，它对这个目录有读写的权限
我使用 crond 定期执行一个 shell 脚本来实现定期 git pull, 并且将 cornd 执行日志， shell 脚本执行日志使用了 logrotate 防止它过大
它使用alpine linux

## web-app container
web-app container 作为我的网站主体，使用 python flask 3.x 开发, 使用 python:3.9 slim 作为image
它同样挂载docker volumes, 但是对其只有读的权限，他会去这个目录下拿取我的 markdown 文章
首先提取 metadata 插入数据库，然后处理文章的内容，我使用 python-markdown 将其渲染为 html 并且存放在某一个目录下
并将这个目录注册为一个staic folder, 这样子 flask 路由函数就可以找到这些 html
为了实现一些

# future consider

1/ add nginx container as reverse proxy
2/ try to use bootstrap5 to opt the css effect
3/ connect to sqlite database to show the data in the sqlite










