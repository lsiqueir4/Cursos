
with open('pessoas.csv') as arquivo: #o with vai permitir que o python feche o arquivo automaticamente
    for registro in arquivo:
        print ('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) 
        #.strip tira o caracter da string, no caso o espaço, split vai quebrar a linha

if arquivo.closed:
    print('arquivo fechado')