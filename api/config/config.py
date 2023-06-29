import os
from decouple import config
from datetime import timedelta



BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SECRET_KEY = os.getenv('SECRET_KEY', default='my-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    # cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
    CACHE_TYPE = os.getenv('CACHE_TYPE')


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
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')  # !!!!!!!!!
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        # SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


config_dict = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}