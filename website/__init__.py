from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
#Create datebase object

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .hangman import hangman
    from .auth import auth

    # Registering blueprints
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(hangman, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app) 

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    # Given *user_id*, return the associated User object.
    def load_user(id):
        return User.query.get(int(id))
    return app


def create_database(app) -> None:
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
