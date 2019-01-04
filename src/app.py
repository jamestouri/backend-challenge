from flask import Flask

from .config import app_config
from .models import db

from .views.CommentView import comment_api as comment_blueprint


def create_app(env_name):
    """Create app"""

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.register_blueprint(comment_blueprint, url_prefix='/api/v1/comments')


    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        return 'comment page'
    return app
