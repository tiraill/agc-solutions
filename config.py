import os

basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nifdl>jfdfmddj@gh'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or f'sqlite:///{TOP_LEVEL_DIR}/shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Uploads
    UPLOADED_PREFIX = 'img/steps/upload/'
    UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/agc_app/static/img/steps/upload'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/steps/upload'

    UPLOADED_PHOTOS_DEST = TOP_LEVEL_DIR + '/agc_app/static/img/steps/upload'
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/steps/upload'

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.yandex.r'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_SENDER = os.environ.get('MAIL_SENDER') or 'dev@eleven-group.ru'
    # MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER') or 'dev@eleven-group.ru'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS') or '9M5mUmL8GC'

    CLEAR_DATABASE = os.environ.get('CLEAR_DATABASE') or 0
    CREATE_ADMIN = os.environ.get('CREATE_ADMIN') or 0

    ADMIN_MAIL = os.environ.get('ADMIN_MAIL')
    ADMIN_PASS = os.environ.get('ADMIN_PASS')
