import os

host = os.environ.get('APP_HOST', '0.0.0.0')
port = os.environ.get('APP_PORT', 7100)
db_name = os.environ.get('DB_NAME', 'testdb')
db_user = os.environ.get('DB_USER', 'test')
db_password = os.environ.get('DB_PASSWORD', 'password')


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'XXXXX' #todo: should be changed for production
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@database:5432/{}".format(db_user, db_password, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


configs = {"dev": DevelopmentConfig, "prod": ProductionConfig}
config = configs[os.environ.get('ENV', 'dev')]
