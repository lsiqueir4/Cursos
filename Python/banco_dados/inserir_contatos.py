from bd import nova_conexao
from mysql.connector import ProgrammingError

inserir_contatos = "INSERT INTO contatos (nome, tel) VALUES (%s, %s) "
args = ('Lucas', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(inserir_contatos, args)
        conexao.commit() #commitar o comando
    except ProgrammingError as e:
        print (f'ERRO: {e.msg}')
    else:
        print ('REGISTRO INCLUIDO, ID:', cursor.lastrowid)