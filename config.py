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

    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "YYYYYYY" #todo: should be changed for production

    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"
    SECURITY_RESET_URL = "/reset/"

    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"
    SECURITY_POST_RESET_VIEW = "/admin/"

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


configs = {"dev": DevelopmentConfig, "prod": ProductionConfig}
config = configs[os.environ.get('ENV', 'dev')]
