from distutils.log import debug
from flask import Flask, request
from flask_restful import Resource, Api
from models import Atividades, Pessoas, Usuarios
from flask_httpauth import HTTPBasicAuth #lib de autenticacao de usuario

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'rafael':'123',
#     'galleani':'321'
# }

# @auth.verify_password #decorador da lib auth
# def verificacao(login, senha):
#     print('Validando usuario')
#     print(USUARIOS.get(login) == senha)
#     if not (login, senha):
#         return False #se não for informado login e senha, retorna False
#     return USUARIOS.get(login) == senha
    
@auth.verify_password #decorador da lib auth
def verificacao(login, senha):
    if not(login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    #para acessar esse metodo, necessário estar logado
    @auth.login_required 
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem':'pessoa nao encontrada'
            }
        return response
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade=dados['idade']
        pessoa.save()
        response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id':pessoa.id
            }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem':'pessoa excluida com sucesso'}

class ListaPessoas(Resource):
    @auth.login_required 
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {'id':pessoa.id,
                 'nome':pessoa.idade,
                 'idade':pessoa.idade
                 }  
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades= Atividades.query.all()
        response = [{'id':i.id, 
                    'nome':i.nome, 
                    'pessoa':i.pessoa.nome} for i in atividades]

    def post(self):
        dados=request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)