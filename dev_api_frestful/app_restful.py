from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import ListaHabilidades
from desenvolvedores import ListaDesenvolvedores, desenvolvedores
import json

app = Flask(__name__)
api = Api(app)


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return (response)


    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}




api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades,'/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)