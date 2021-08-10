from flask_restful import Resource

habilidades = ['Python', 'Java', 'Flask', 'PHP']

class ListaHabilidades(Resource):
    def get(self):
        return habilidades
