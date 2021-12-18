try:
    from mysql import connect
except:
    print ('BIBLIOTECA NAO INSTALADA')
else:
    print ('BIBLIOTECA INSTALADA E OK')


conexao = connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda') #.execute executa um comando em sqls