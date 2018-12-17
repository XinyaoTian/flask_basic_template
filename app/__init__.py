from flask import Flask
from config import Config


# db = SQLAlchemy()
# migrate = Migrate()
# login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = _l('Please log in to access this page.')
# mail = Mail()
# bootstrap = Bootstrap()
# moment = Moment()
# babel = Babel()

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
    # babel.init_app(app)

    # import errors blueprint
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # import main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


