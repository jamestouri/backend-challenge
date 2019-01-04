from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .CommentModel import CommentModel, CommentSchema
