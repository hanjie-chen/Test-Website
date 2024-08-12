from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 导入所有模型，以确保它们被SQLAlchemy识别
from .articles import Article
