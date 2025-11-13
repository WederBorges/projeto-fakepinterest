#Model contém a estrutura do banco de dados

from pinterest import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(id)
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, nullable=False, unique=True) 
    senha = db.Column(db.String, nullable=False)
    fotos = db.relationship("Foto", backref='user', lazy='select')



class Foto(db.Model):
    id_foto = db.Column(db.Integer, primary_key=True) 
    imagem = db.Column(db.String, default="default.png") 
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc)) 
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False) 

