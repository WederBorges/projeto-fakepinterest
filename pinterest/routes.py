#cria as rotas do site


from pinterest import app, bcrypt, db
from flask import render_template, url_for
from pinterest.forms import FormLogin, CriarConta
from pinterest.models import Usuario, Foto


@app.route("/", methods=['GET', 'POST'])
def home():
    form_login = FormLogin()
    return render_template('homepage.html', form=form_login)


@app.route("/criar-conta", methods=['GET', 'POST'])
def criar_conta():
    form_criar_conta = CriarConta()

    if form_criar_conta.validate_on_submit():
        usuario = Usuario()
        usuario.username = form_criar_conta.user_name.data
        usuario.email = form_criar_conta.email.data
        usuario.senha = bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('UTF-8')
        db.session.add(usuario)
        db.session.commit()
        print("VALIDOU")
    else:
        print("Validou não.")


    return render_template('criarconta.html', form=form_criar_conta)


@app.route("/perfil/<id_usuario>")
def perfil(id_usuario):
    return render_template('perfil.html', id_usuario=id_usuario)
