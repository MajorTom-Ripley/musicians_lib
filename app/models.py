import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Настройка базы данных
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "musicians.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель данных для пользователей
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Модель данных для музыкантов
class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instrument = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    song = db.Column(db.String(200), nullable=False)

# Функция для создания базы данных, если она не существует
def create_db():
    if not os.path.exists(os.path.join(BASE_DIR, 'instance', 'musicians.db')):
        db.create_all()
        print("База данных создана!")
    else:
        print("База данных уже существует!")

# Вызов функции создания базы данных
with app.app_context():
    create_db()
