from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config
import psycopg2

#db_connection = psycopg2.connect("dbname=test, user=postgres password=")

db = SQLAlchemy()

def create_app():
    from .models import User
    app = Flask(__name__)



    app.config['SECRET_KEY'] = config('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)

    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()