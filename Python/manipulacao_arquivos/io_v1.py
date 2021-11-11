arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines(): #.splitlines le cada uma das linhas separadas
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))