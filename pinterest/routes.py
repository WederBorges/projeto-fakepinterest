#cria as rotas do site


from pinterest import app, bcrypt, db
from flask import render_template, url_for, redirect
from pinterest.forms import FormLogin, CriarConta
from pinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user

@app.route("/", methods=['GET', 'POST'])
def home():
    
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('homepage.html', form=form_login)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/criar-conta", methods=['GET', 'POST'])
def criar_conta():
    
    form_criar_conta = CriarConta()

    if form_criar_conta.validate_on_submit():
        usuario = Usuario(
            username=form_criar_conta.user_name.data,
            email=form_criar_conta.email.data,
            senha= bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('UTF-8')) #senha criptografada
        db.session.add(usuario)
        db.session.commit()
        login_user(usuario, remember=True   )
        print("VALIDOU")
        return redirect(url_for('perfil', id_usuario=usuario.id))
    else:
        print("Validou não.")
    return render_template('criarconta.html', form=form_criar_conta)


@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    
    usuario = Usuario.query.get(int(id_usuario))
    if not usuario:
        return "Usuário não encontrado", 404
    if int(id_usuario) == int(current_user.id):
        return render_template('perfil.html', usuario=current_user)
    else:
        return render_template('perfil.html', usuario=usuario)
