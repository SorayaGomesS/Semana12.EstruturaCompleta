import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Variáveis de ambiente
    app.config['API_KEY'] = os.environ.get('API_KEY')
    app.config['API_URL'] = os.environ.get('API_URL')
    app.config['API_FROM'] = os.environ.get('API_FROM')
    app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
    app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

    # Inicializa extensões
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Importa e registra as rotas
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
