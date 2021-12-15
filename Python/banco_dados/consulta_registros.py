from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    try:
        cursor.execute(sql)
        contatos = cursor.fetchall() #carrega todos os registros disponiveis e retorna uma lista
    except ProgrammingError as e:
        print (f'ERRO: {e.msg}')
    else:
        for contato in contatos:
            print (f'{contato[2]:2d} - {contato[0]:10s} Tel: {contato[1]}') #indice 2 - ID, 2d = 2 digitos, 10s = 10 Caracteres