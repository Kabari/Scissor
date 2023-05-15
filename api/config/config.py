import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpth(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY', default='my-secret-key')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

config_dict = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}