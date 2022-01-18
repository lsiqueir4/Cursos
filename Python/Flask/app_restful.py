from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {'id':0,'nome': 'Rafael', 'habilidades': ['Python','Flask']},
    {'id':1,'nome': 'Galleani', 'habilidades': ['Python', 'Django']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try: 
            dev = devs[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            dev = {'status':'erro', 
            'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o adm da API'
            dev = {'status':'erro', 
            'mensagem': mensagem}
        return dev
    def put(self, id):
        dados = json.loads(request.body)
        devs[id] = dados
        return dados
    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}

class ListaDevs(Resource):
    def post(self): #criar um novo dev, o ID sera o lenght da lista de devs
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return {'status' :'sucesso', 'mensagem': 'registro inserido'}
    def get(self): #retorna toda a lista de devs
        return devs

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDevs, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)