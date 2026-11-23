from datetime import datetime
from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, and_, func

from routes import post_fabricante, post_fornecedor, post_pastilha, post_funcionario, get_pastilha, get_fornecedor, \
    get_fabricante

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dashboard')
def dashboard():
    pastilhas_resultado = get_pastilha()
    fabricantes_resultado = get_fabricante()
    fornecedores_resultado = get_fornecedor()
    return render_template("dashboard.html", qtd_pastilhas=len(pastilhas_resultado["pastilha"]),
                           qtd_fabricantes=len(fabricantes_resultado["fabricante"]),
                           qtd_fornecedores=len(fornecedores_resultado["fornecedor"]))


@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        if not nome or not email or not senha:
            print('Valores não encontrados')
            return redirect(url_for('funcionarios'))
        try:
            print("Cadastrando funcionario...")
            post_funcionario(nome=nome, email=email, senha=senha)
            return redirect(url_for('pastilhas'))

        except Exception as e:
            print(f'ERROR: {e}')
            redirect(url_for('funcionarios'))

    return render_template("login.html")


@app.route('/pastilhas', methods=['GET', 'POST'])
def pastilhas():
    if request.method == 'POST':
        aplicacao = request.form.get('form-uso')
        material = request.form.get('form-material')
        cor = request.form.get('form-cor')
        fornecedor_id = request.form.get('form-fornecedor_id')

        if not aplicacao or not material or not cor:
            print('Valores não encontrados')
            return redirect(url_for('pastilhas'))
        try:
            print("Cadastrando empresa...")
            post_pastilha(aplicacao=aplicacao, material=material, cor=cor, fornecedor_id=fornecedor_id)
            return redirect(url_for('pastilhas'))

        except Exception as e:
            print(f'ERROR: {e}')
            redirect(url_for('pastilhas'))

    pastilhas_resultado = get_pastilha()
    print("foi", pastilhas_resultado)
    return render_template("pastilhas.html", listar_pastilha=pastilhas_resultado["pastilha"])


@app.route('/fornecedores', methods=['GET', 'POST'])
def fornecedores():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        email = request.form.get('form-email')
        cnpj = request.form.get('form-cnpj')

        if not nome or not cnpj or not email:
            print('Valores não encontrados')
            return redirect(url_for('fornecedores'))
        try:
            print("Cadastrando empresa...")
            post_fornecedor(nome=nome, email=email, cnpj=cnpj)
            return redirect(url_for('pastilhas'))

        except Exception as e:
            print(f'ERROR: {e}')
            redirect(url_for('fornecedores'))

    fornecedores_resultado = get_fornecedor()
    print("foi", fornecedores_resultado)
    return render_template("cadastro_forn.html", listar_fornecedor=fornecedores_resultado["fornecedor"])


@app.route('/fabricantes', methods=['GET', 'POST'])
def fabricantes():
    if request.method == 'POST':
        empresa = request.form.get('form-empresa')
        cnpj = request.form.get('form-cnpj')

        if not empresa or not cnpj:
            print('Valores não encontrados')
            return redirect(url_for('fabricantes'))
        try:
            print("Cadastrando empresa...")
            post_fabricante(nome=empresa, cnpj=cnpj)
            return redirect(url_for('pastilhas'))

        except Exception as e:
            print(f'ERROR: {e}')
            redirect(url_for('fabricantes'))

    fabricantes_resultado = get_fabricante()
    print("foi", fabricantes_resultado)
    return render_template("cadastro_fabr.html", listar_fabricante=fabricantes_resultado["fabricante"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        # print(email, senha)

        return redirect(url_for('pastilhas'))

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, port=5051)
