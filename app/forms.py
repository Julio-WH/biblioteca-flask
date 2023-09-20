from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contrasenia', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class AuthorForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    lastname = StringField('Apellidos', validators=[DataRequired()])
    email = StringField('Email')
    submit = SubmitField('Aceptar')
