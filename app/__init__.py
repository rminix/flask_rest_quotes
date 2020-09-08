from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)

    from app.resources.homepage import Home
    api.add_resource(Home, '/')

    return app