#leitura por streaming, melhor para arquivos grandes
arquivo = open('pessoas.csv')
for registro in arquivo:
    print ('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) #.strip tira o caracter da string, no caso o espaço, split vai quebrar a linha
arquivo.close()