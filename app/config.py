import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
            'SQLALCHEMY_TRACK_MODIFICATIONS',False)
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    pass