# app/forms.py
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[Optional(), Length(max=100)])
    surname = StringField('Фамилия', validators=[Optional(), Length(max=100)])
    patronymic = StringField('Отчество', validators=[Optional(), Length(max=100)])
    profile_pic = FileField('Фото профиля')
    submit = SubmitField('Сохранить изменения')
    