from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25) #insert
    print(pessoa)
    pessoa.save() #commit

def consulta_todos():
    pessoa=Pessoas.query.all() #select
    for i in pessoa:
        print(i)
    
def consulta_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani') # select com where
    for p in pessoa:
        print(p)
    
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani') 
    pessoa.idade = 20 #update
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani')
    pessoa.delete() #funcao criada no arquivo models

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__=='__main__':
    insere_usuario('rafael', '1234')
    insere_usuario('galleani', '4321')
    consulta_todos_usuarios()
    #consulta_todos()
    #consulta_pessoa()