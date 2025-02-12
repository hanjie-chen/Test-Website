# About the website

这是我正在开发的个人网站，目前的主要功能是作为我的个人博客网站，它目前由2个container组成
web-app contianer 作为网站的主体内容，使用python flask 3.x 开发，它会去某个路径下拿到我的markdown笔记文章，并且将其渲染为html, 然后返回给用户，这个路径其实是一个docker volume

articles-sync container 这是管理我的markdown笔记文章的container, 因为我的笔记文章存放在github 上面，并且会是不是的更新，所以我将其放到一个docker volume中并且挂载到articles-sync的某个路径中，让其每天定时更新，这个contianer由读写权限，而web-app container只有读的权限

目前还在开发阶段，所以只有这2个contianer

# future consider

## docker consider
add nginx container as reverse proxy

配置nginx 策略，先不考虑 waf

## web app consider







