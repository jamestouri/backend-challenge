
from marshmallow import (
    fields,
    Schema,
)
import datetime
from . import db

class CommentModel(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)


    def __init__(self, data):
        self.title = data.get('title')
        self.body = data.get('body')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
          setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_comments():
        return CommentModel.query.all()

    @staticmethod
    def get_one_comment(id):
        return CommentModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
