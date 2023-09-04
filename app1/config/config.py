import datetime
import pymysql
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

# basedir = os.path.abspath(os.path.dirname(__file__))


# def create_sqlite_uri(db_name):
#     return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig: 
    SECRET_KEY = 'THIS IS MAX'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)
    TEMPLATES_AUTO_RELOAD = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/data"
 

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    # SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/test"
 

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
