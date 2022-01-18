from models import Pessoas

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

if __name__=='__main__':
    #insere_pessoas()
    #consulta_todos()
    consulta_pessoa()