from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {'id':0,'nome': 'Rafael', 'habilidades': ['Python','Flask']},
    {'id':1,'nome': 'Galleani', 'habilidades': ['Python', 'Django']}
]

#devolve um dev pelo ID, tambem altera e deleta um dev
@app.route('/dev/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':  #qnd em metodo get, ele vai pegar o json pelo ID
        try:
            dev = devs[id]
            return jsonify(dev)
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            dev = {'status':'erro', 
            'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o adm da API'
            dev = {'status':'erro', 
            'mensagem': mensagem}
    elif request.method =='PUT': #qnd metodo put, ele vai inserir, alterar o json 
        dados = json.loads(request.body)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE': #metodo delete vai deletar o registro referente ao ID informado
        devs.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})

#Lista todos os devs e permite registrar um novo dev
@app.route('/dev/', methods = ['GET', 'POST'])
def lista_devs():
    if request.method == 'POST': #criar um novo dev, o ID sera o lenght da lista de devs
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify({'status' :'sucesso', 'mensagem': 'registro inserido'})
    elif request.method == 'GET': #retorna toda a lista de devs
        return jsonify(devs)


if __name__=='__main__':
    app.run(debug=True)
