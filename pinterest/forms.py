#o forms mantém os formulários do nosso site
from models import Usuario
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class FormLogin(): 
    email = StringField("E-mail", validators=[DataRequired(), Email(), Length(100)])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")
    

class CriarConta():
    user_name = StringField("Nome de Usuário", validators=[DataRequired])
    email = StringField("E-mail", validators=[DataRequired(), Email(), Length(100)])
    senha = PasswordField("Senha", validators=[DataRequired,PasswordField(), Length(6, 20)])
    senha_confirmacao = PasswordField("Confirmar Senha", validators=[DataRequired,PasswordField(), Length(6, 20), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")

    def validate_email(self):
        usuario = Usuario.query.get()  