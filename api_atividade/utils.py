from models import Pessoas, db_session, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Alves', idade=25)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Alves').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alves').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jean').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Marcelo', '1232')
    insere_usuario('Eduardo', '1234')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()