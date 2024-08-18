from . import db

# 文章元数据
class Article_Meta_Data(db.Model):
    # 指定数据模型在数据库中的表名称 如果未指定那么为类名称的小写
    __tablename__ = 'article_meta_date'
    # 主键 但是无需为其赋值 SQLite数据库会自动为其生成一个唯一的值
    id = db.Column(db.Integer, primary_key = True)
    # 文章标题 最长不超过100个字 不能为空
    title = db.Column(db.String(100), nullable = False)
    # 文章发布时间
    rollout_date = db.Column(db.Date, nullable = False)
    # 表示文章最后更新的日期 只精确到年月日
    ultimate_modified_date = db.Column(db.Date, nullable = False)
    # 文章作者
    author = db.Column(db.String(50), nullable = False)
    # 文章指导者 可以为空
    instructor = db.Column(db.String(50), nullable = True)
    # 文章内容简介
    brief_introduction = db.Column(db.Text, nullable = True)
    # 文章封面链接
    cover_image_url = db.Column(db.String(100), nullable = False)
    # 文章分类
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category')

    def __repr__(self):
        return f'<Article {self.title}>'

class Article_Category(db.Model):
    __tablename__ = 'articl_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    children = db.relationship('Category')
