import requests

endereco = "http://10.135.232.21:5004"

def get_pastilha():
    url = f"{endereco}/listar_pastilha"

    result_pastilha = requests.get(url)

    return result_pastilha.json()


def get_fabricante():
    url = f"{endereco}/listar_fabricante"

    result_fabricante = requests.get(url)

    return result_fabricante.json()


def get_fornecedor():
    url = f"{endereco}/listar_fornecedor"

    result_fornecedor = requests.get(url)

    return result_fornecedor.json()


def get_funcionario():
    url = f"{endereco}/listar_funcionario"

    result_funcionario = requests.get(url)

    return result_funcionario.json()

def get_movimentacao():
    url = f"{endereco}/listar_movimentacao"

    result_movimentacao = requests.get(url)

    return result_movimentacao.json()


def post_pastilha(tipo_aplicacao, cor, material, fornecedor_id):
    url = f"{endereco}/cadastro_pastilha"

    dados = {
        "tipo_aplicacao": tipo_aplicacao,
        "cor": cor,
        "material": material,
        "fornecedor_id": fornecedor_id
    }

    result_pastilha = requests.post(url, json=dados)

    return result_pastilha.json()

def post_fabricante(nome, cnpj):
    url = f"{endereco}/cadastro_fabricante"

    dados = {
        "nome": nome,
        "cnpj": cnpj
    }

    result_fabricante = requests.post(url, json=dados)

    print('Mavi',result_fabricante)

    return result_fabricante.json()


def post_fornecedor(nome, cnpj, email):
    url = f"{endereco}/cadastro_fornecedor"

    dados = {
        "nome": nome,
        "email": email,
        "cnpj": cnpj,
    }

    result_fornecedor = requests.post(url, json=dados)


    return result_fornecedor.json()

def post_funcionario(nome, email, senha):
    url = f"{endereco}/cadastro_funcionario"

    dados = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    result_funcionario = requests.post(url, json=dados)

    return result_funcionario.json()

def post_movimentacao(quantidade, pastilha_id, tipo):
    url = f"{endereco}/cadastro_movimentacao"

    dados = {
        "quantidade": quantidade,
        "pastilha_id": pastilha_id,
        "tipo": tipo
    }

    result_movimentacao = requests.post(url, json=dados)

    return result_movimentacao.json()






