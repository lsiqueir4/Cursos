from bd import nova_conexao
from mysql.connector import ProgrammingError

mostrar_tabelas = 'SHOW TABLES'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(mostrar_tabelas)
            for i, database in enumerate(cursor, start=1):
                print (f'Tabela {i}: {database[0]}')
            print ('SUCESSO')
        except ProgrammingError as e:
            print(f'ERRO INTERNO:{e.msg}')
except ProgrammingError as e:
    print('ERRO CONEXAO')


