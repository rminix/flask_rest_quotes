from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    api = Api(app)
    if app.config["ENV"] == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)


    db.init_app(app)


    from app.resources.homepage import Home
    api.add_resource(Home, '/')
    from app.resources.quotes import Quotes
    api.add_resource(Quotes, '/api/quote/create')
    from app.resources.quotes import RandomQuote
    api.add_resource(RandomQuote, '/api/quote/random')


    with app.app_context():
        db.create_all()
    return app