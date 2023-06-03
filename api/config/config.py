import os
from decouple import config
from datetime import timedelta



BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY', default='my-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False




    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=24)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    # cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
    CACHE_TYPE = config('CACHE_TYPE')

    # MAIL_SERVER = 'smtp@gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'kabariirenaeus@gmail.com'
    # MAIL_PASSWORD = 'dlrkfjyclgbhthuw'
    # MAIL_DEFAULT_SENDER = 'kabariirenaeus@gmail.com'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    pass


config_dict = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}