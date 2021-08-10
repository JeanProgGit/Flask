from flask import request
from flask_restful import Resource
import json
desenvolvedores = [
    {
    'id':'0',
    'nome': 'Jean',
    'habilidades':['Python', 'Flask']
     },
    {
    'id':'1',
    'nome': 'Alves',
    'habilidades':['Python', 'Django']}
]

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]