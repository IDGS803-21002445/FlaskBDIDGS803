from slqalchemy import create_engine

class Config(object):
    SECRET_KEY="ClaveSecreta"
    SESSION_COOKIE_SECURE=False

Class DevelopmentConfig(Config):
    DEBUG = True
    SQLACHEMY_DATABASE_URI='mysql+pymysql://josuearmandoriverahernandez:root@127.0.0.1/bdigs803'
    SQLACHEMY_TRACK_MODIFICATIONS = False