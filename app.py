from datetime import datetime
from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, and_, func

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cadastro_func')
def funcionarios():
    return render_template("cadastro_func.html")

@app.route('/pastilhas')
def pastilhas():
    return render_template("pastilhas.html")

@app.route('/fornecedores')
def fornecedores():
    return render_template("cadastro_forn.html")

@app.route('/fabricantes')
def fabricantes():
    return render_template("cadastro_fabr.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('form-cpf')
        senha = request.form.get('form-senha')

        print(cpf, senha)

        return redirect(url_for('pastilhas'))

    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
