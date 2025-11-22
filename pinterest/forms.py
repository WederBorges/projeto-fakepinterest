#o forms mantém os formulários do nosso site
from .models import Usuario
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class FormLogin(FlaskForm): 
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()  

        if not usuario:
            raise ValidationError("Não existe conta para este e-mail")
    

class CriarConta(FlaskForm):
    user_name = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=20)])
    senha_confirmacao = PasswordField("Confirmar Senha", validators=[DataRequired(), Length(min=6, max=20), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()  

        if usuario:
            raise ValidationError("Já existe conta para este e-mail")
        

class FormEnviarFoto(FlaskForm):

    foto = FileField("Foto", validators=[DataRequired()])
    botao_upload = SubmitField("Enviar Foto")      