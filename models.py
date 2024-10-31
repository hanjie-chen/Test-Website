from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Date, Text, Integer
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# 文章元数据
class Article_Meta_Data(db.Model):
    # 指定数据模型在数据库中的表名称 如果未指定那么为类名称的小写
    __tablename__ = 'article_meta_date'
    # 主键 但是无需为其赋值 SQLite数据库会自动为其生成一个唯一的值
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # 文章标题 最长不超过100个字 默认nullable=False
    title: Mapped[str] = mapped_column(String(100))

    # 文章发布时间
    rollout_date: Mapped[date] = mapped_column(Date)

    # 表示文章最后更新的日期 只精确到年月日
    ultimate_modified_date: Mapped[date] = mapped_column(Date)

    # 文章作者 最长不超过50个字符
    author: Mapped[str] = mapped_column(String(50))

    # 文章指导者 存在Optional 默认nullable=True
    instructor: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 文章内容简介
    brief_introduction: Mapped[str] = mapped_column(Text)

    # 文章封面链接
    cover_image_url: Mapped[str] = mapped_column(String(100))

    # 文章分类
    category: Mapped[str] = mapped_column(String(100))
    
    # 文章分类 使用 mptt 待开发和测试
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # category = db.relationship('Category')

    def __repr__(self):
        return f'<Article {self.title}>'

# mptt 待开发和测试
# class Article_Category(db.Model):
#     __tablename__ = 'articl_category'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False, unique=True)
#     parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
#     children = db.relationship('Category')
