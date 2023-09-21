from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.widgets import CheckboxInput
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


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = SelectField('Autor', coerce=int, validators=[DataRequired()])
    pub_date = DateField('Publication Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Aceptar')

