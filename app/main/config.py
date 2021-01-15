import os

mysql_config = {
	'host': os.environ.get('MYSQL_HOST', 'localhost'),
	'user': os.environ.get('MYSQL_USER', 'root'),
	'pass': os.environ.get('MYSQL_PASS', ''),
	'db':   os.environ.get('MYSQL_DB', 'flask_prac'),
}

class Config:
	SECRET_KEY = "mynameisseungjaekim"
	DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

SECRET_KEY = Config.SECRET_KEY