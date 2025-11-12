#cria as rotas do site


from pinterest import app
from flask import render_template, url_for


@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/perfil/<id_usuario>")
def perfil(id_usuario):
    return render_template('perfil.html', id_usuario=id_usuario)
