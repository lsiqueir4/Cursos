#imprime em um novo arquivo
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida: #vai criar um novo arquivo txt 
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print ('Nome: {}, Idade: {}'.format(*pessoa), file=saida) 
            #o print sera impresso no arquivo criado
            

if arquivo.closed:
    print('arquivo fechado')

if saida.closed:
    print('arquivo de saida fechado')