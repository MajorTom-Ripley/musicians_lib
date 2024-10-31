# app/routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import db, User, Musician
from .forms import LoginForm, RegistrationForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    musicians_list = Musician.query.all()
    return render_template('musicians.html', musicians=musicians_list)

@main.route('/musician/<int:id>')
def musician_detail(id):
    musician = Musician.query.get_or_404(id)
    return render_template('musician_detail.html', musician=musician)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Проверяем, если пользователь уже аутентифицирован
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Неверное имя пользователя или пароль.')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # Проверяем, если пользователь уже аутентифицирован
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Пользователь с таким именем уже существует.')
            return render_template('register.html', form=form)
        
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались. Пожалуйста, войдите.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из системы.')
    return redirect(url_for('main.home'))

@main.route('/albums')
def albums():
    # Логика для получения альбомов
    return render_template('albums.html')
