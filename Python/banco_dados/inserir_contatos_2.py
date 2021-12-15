from bd import nova_conexao
from mysql.connector import ProgrammingError

inserir_contatos = "INSERT INTO contatos (nome, tel) VALUES (%s, %s) "
args = (
    ('Lucas', '98765-4321'),
    ('Luca', '98452-4321'),
    ('Gui', '98333-4322'),
    ('Ana', '98865-4325'),
    ('Beca', '99865-4321'),
    ('Pedro', '97655-4333'))

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(inserir_contatos, args) #varios executes
        conexao.commit() #commitar o comando
    except ProgrammingError as e:
        print (f'ERRO: {e.msg}')
    else:
        print (f'Foi(ram) incluido(s) {cursor.rowcount} registro(s)!') #quantidade de registros incluidos