from bd import nova_conexao
from mysql.connector import ProgrammingError

excluir_tabela = "DROP TABLE emails"

try:
    with nova_conexao() as conexao:
        try: 
            cursor = conexao.cursor()
            cursor.execute(excluir_tabela)
        except ProgrammingError as e:
            print(f'ERRO: {e.msg}')
except ProgrammingError as e:
    print(f'ERRO DE CONEXAO')

