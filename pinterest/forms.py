#o forms mantém os formulários do nosso site
from .models import Usuario
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class FormLogin(FlaskForm): 
    email = StringField("E-mail", validators=[DataRequired(), Email(), Length(100)])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")
    

class CriarConta(FlaskForm):
    user_name = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=20)])
    senha_confirmacao = PasswordField("Confirmar Senha", validators=[DataRequired(), Length(min=6, max=20), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first  

        if usuario:
            return ValidationError("Já existe conta para este e-mail")