from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    api = Api(app)

    db.init_app(app)


    from app.resources.homepage import Home
    api.add_resource(Home, '/')


    with app.app_context():
        db.create_all()
    return app