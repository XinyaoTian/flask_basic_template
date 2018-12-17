from flask import Flask, current_app, request
from config import Config
# I18n & L10n
from flask_babel import Babel
# mail server
import logging
from logging.handlers import SMTPHandler
# error handling
from logging.handlers import RotatingFileHandler
import os


# db = SQLAlchemy()
# migrate = Migrate()
# login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = _l('Please log in to access this page.')
# mail = Mail()
# bootstrap = Bootstrap()
# moment = Moment()
babel = Babel()


# using factory model
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # migrate.init_app(app, db)
    # login.init_app(app)
    # mail.init_app(app)
    # bootstrap.init_app(app)
    # moment.init_app(app)
    babel.init_app(app)

    # import errors blueprint
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # import main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Using SMTP to send email
    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
                secure = None
                if app.config['MAIL_USE_TLS']:
                    secure = ()
                mail_handler = SMTPHandler(
                    mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                    fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                    toaddrs=app.config['ADMINS'], subject='Microblog Failure',
                    credentials=auth, secure=secure
                )
                mail_handler.setLevel(logging.ERROR)
                app.logger.addHandler(mail_handler)
        # Logging file
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/web_application.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Flask based web app startup')

    return app


# for I18n and L10n
@babel.localeselector
def get_locale():
    # # Auto-select preference language
    # return request.accept_languages.best_match(current_app.config['LANGUAGES'])
    # Force to return Chinese
    return 'zh'

