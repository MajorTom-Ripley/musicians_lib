from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# Модель данных для пользователей
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    
    # Новые поля для имени, фамилии, отчества и фото профиля
    name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    patronymic = db.Column(db.String(100), nullable=True)
    profile_pic = db.Column(db.String(200), nullable=True, default='default.jpg')

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
    youtube_video_url = db.Column(db.String)
    rutube_video_url = db.Column(db.String)
    plvideo_video_url = db.Column(db.String)
