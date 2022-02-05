from web_app import app
from flask import render_template, redirect, url_for
from web_app.models import Info, Usuario
from web_app.forms import RegistroForm, RegistroInfo
from web_app import db
@app.route("/")
@app.route('/home')
def home_page():    
    return render_template('home.html')
    
@app.route('/consulta')
def consulta():
    items = Usuario.query.all()
    return render_template('consulta.html', items=items)

@app.route('/adm', methods=['GET', 'POST'])
def adm():
    form = RegistroForm()
    if form.validate_on_submit():
        user_to_creat = Usuario(name=form.name.data,email=form.email.data, senha=form.senha.data)
        db.session.add(user_to_creat)
        db.session.commit()
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'Erro ao criar usuario: {err_msg}')
    return render_template('adm.html', form = form)

@app.route('/info', methods=['GET', 'POST'])
def info():    
    form = RegistroInfo()
    if form.validate_on_submit():
        info_to_create = Info(marca=form.marca.data,desc=form.desc.data,img=form.img.data)
        db.session.add(info_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'Erro ao criar info: {err_msg}')
    return render_template('info.html', form = form)   