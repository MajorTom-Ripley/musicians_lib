from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Инициализация SQLAlchemy с экземпляром Flask
    login_manager.init_app(app)  # Инициализация Flask-Login

    # Определение функции user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .models import User, Musician  # Импорт моделей

    # Создание базы данных, если она не существует
    with app.app_context():
        db_path = os.path.join(app.config['SQLALCHEMY_DATABASE_URI'].split('///')[1])
        if not os.path.exists(db_path):
            db.create_all()
            print("База данных создана")
        else:
            print("База данных уже существует")

    from .routes import main
    app.register_blueprint(main)

    return app
