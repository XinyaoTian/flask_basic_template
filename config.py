import os


class Config(object):
    # safety key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # I18n & L10n
    LANGUAGES = ['en', 'zh']

    # mail server
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['devops2048@gmail.com']

