import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:passwd@0.0.0.0:3306/snaqme'
    SQLALCHEMY_TRACK_MODIFICATIONS = False