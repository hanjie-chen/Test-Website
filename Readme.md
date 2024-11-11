# About the website

This is the Frontend website of my personal website. Lask time I try to develop frontend and backend in both, but actaully failed because I stuck in the backend database desing and deploy.

Now I trying to develop the backend part of my website, I'd to choose the SQLite as my database to store my articles.



# About the requirements

```
markdown2[all]
Flask >= 3.x
Flask-SQLalchemy >= 3.x
SQLAlchemy >= 2.x
frontmatter
```


# About the website icon design

[Yesicon - 精选全球高品质、开源、免费的矢量图标库](https://yesicon.app/?lang=zh-hans)

use that website to get icon



# LLM Prompt

## Backend

我正在搭建一个个人网站，使用python Flask框架，CSS采用Bootstrap5，数据库采用SQLite，并且使用SQLAlchemy和Flask-SQLAlchemy扩展来访问SQLite数据库。我打算将网站部署到一块树莓派4B上面。

我打算使用这个网站发布一些自己写的文章，包括技术类的，还有生活类的，还有自己的思考，文章使用markdown及其扩展语法。我打算将文章的元数据包括文章标题，文章封面图片链接，文章最后修改日期，文章作者，文章指导者，文章分类，文章简介，存储在sqlite数据库，文章本体则使用markdown编辑器来编辑，一篇文章一个文件夹，其中包含文章和图片文件夹。

网站目前只包含2个部分，首页和文章分类页面。其中首页主要是简单的自我介绍和本网站介绍。文章分类页面包含了文章的分类，以及各个分类之下的文章元数据卡片。我打算使用嵌套集合模型 [Nested Set Model] 来实现文章分类的树形结构

请你在接下来的对话中牢记这些信息。如果你已经记住，请你只回答“明白”

