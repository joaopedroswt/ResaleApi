from flask import Flask, request
import json
from Repositories import Repositories
app = Flask(__name__)


@app.route("/ResaleApi/v1/ListEntidades", methods = ['GET'])
def list_entidades():
    entidade = request.headers['Entidade']

    if entidade == 'IMOVEL':
        imovel = is_imovel()
        return {"Imovel": imovel}
    elif entidade == 'IMOBILIARIA':
        imobiliaria = is_imobiliaria()
        return {"Imobiliaria": imobiliaria}
    else:
        return {"code_error": 404.001, "message": "entidade não encontrada"}

def is_imovel():
    imv = Repositories()

    dados = imv.list_imovel()

    return dados

def is_imobiliaria():
    imv = Repositories()

    dados = imv.list_imobiliaria()

    return dados

@app.route("/ResaleApi/v1/RegisterImovel", methods = ['POST'])
def regsiter_imovel():
    imv = Repositories()
    dados = json.loads(request.data)
    validate = valida_parametros_vazios(dados, 1)

    if validate['CodRetorno'] == '99':
        retorno = validate['Mensagem'], 200
    else:
        retorno = imv.register_imovel_rep(dados)

    return {'Mensagem:': retorno}

@app.route("/ResaleApi/v1/RegisterImobiliaria", methods=['POST'])
def regsiter_imobiliaria():
    imv = Repositories()
    dados = json.loads(request.data)
    validate = valida_parametros_vazios(dados, 0)

    if validate['CodRetorno'] == '99':
        retorno = validate['Mensagem'], 200
    else:
        retorno = imv.register_imobiliaria_rep(dados)

    return {'Mensagem:': retorno}

@app.route("/ResaleApi/v1/EditImobiliaria", methods=['POST'])
def edit_imobiliaria():
    imv = Repositories()
    dados = json.loads(request.data)
    validate = valida_parametros_vazios(dados, 0)

    if validate['CodRetorno'] == '99':
        retorno = validate['Mensagem'], 200
    else:
        retorno = imv.edit_imobiliaria_rep(dados)

    return {'Mensagem:': retorno}

@app.route("/ResaleApi/v1/EditImovel", methods=['POST'])
def edit_imovel():
    imv = Repositories()
    dados = json.loads(request.data)
    validate = valida_parametros_vazios(dados, 1)

    if validate['CodRetorno'] == '99':
        retorno = validate['Mensagem'], 200
    else:
        retorno = imv.edit_imovel_rep(dados)

    return {'Mensagem:': retorno}

@app.route("/ResaleApi/v1/DeleteImobiliaria", methods=['POST'])
def delete_imobiliaria():
    imv = Repositories()
    dados = json.loads(request.data)
    imobiliaria = imv.delete_imobiliaria_rep(dados)

    return {"message": imobiliaria}

@app.route("/ResaleApi/v1/DeleteImovel", methods=['POST'])
def delete_imovel():
    imv = Repositories()
    dados = json.loads(request.data)
    imobiliaria = imv.delete_imovel_rep(dados)

    return {"message": imobiliaria}

def valida_parametros_vazios(param, tipo_execucao):
    #0 é correspondente a IMOBILIARIA
    #1 é correspondente a IMOVEL
    if tipo_execucao == 0:
        if 'NOME' not in param:
            return {'CodRetorno': '99' ,'Mensagem': 'Campo NOME não pode ser vazio.'}
        elif 'ENDERECO' not in param:
            param.update({'ENDERECO': "" })
            return {'CodRetorno': '00' ,'Mensagem': ''}
        else:
            return {'CodRetorno': '00' ,'Mensagem': ''}
    else:
        if 'NOME' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo NOME não pode ser vazio.'}
        elif 'ENDERECO' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo ENDERECO não pode ser vazio.'}
        elif 'DESCRICAO' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo DESCRICAO não pode ser vazio.'}
        elif 'STATUS' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo STATUS não pode ser vazio.'}
        elif 'TIPO' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo TIPO não pode ser vazio.'}
        elif 'IMOBILIARIA' not in param:
            return {'CodRetorno': '99', 'Mensagem': 'Campo IMOBILIARIA não pode ser vazio.'}
        elif 'CARACTERISTICA' not in param:
            param.update({'CARACTERISTICA': ""})
            return {'CodRetorno': '00', 'Mensagem': ''}
        elif 'FINALIDADE' not in param:
            param.update({'FINALIDADE': ""})
            return {'CodRetorno': '00', 'Mensagem': ''}
        else:
            return {'CodRetorno': '00', 'Mensagem': ''}


if __name__ == "__main__":
    app.run()