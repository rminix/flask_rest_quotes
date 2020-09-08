import os
from app.utils.exporter import exporter

if os.getenv('FLASK_ENV') == 'production':
    exporter()

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
db = os.getenv('POSTGRES_DB')


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
            'SQLALCHEMY_TRACK_MODIFICATIONS',False)
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
