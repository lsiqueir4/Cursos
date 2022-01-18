from flask_restful import Resource
from flask import request
import json

habilidades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return habilidades
    def put(self, id):
        dados = json.loads(request.body)
        habilidades[id]= dados
        return dados
    def post(self, id):
        dados = json.loads(request.data)
        posicao = len(habilidades)
        dados['id'] = posicao
        habilidades.append(dados)
    def delete(self):
        habilidades.pop(id)
        return habilidades
