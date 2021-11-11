#leitura por streaming, melhor para arquivos grandes

try: #tenta executar, mesmo se não conseguir, executa o finally
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print ('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) 
        #.strip tira o caracter da string, no caso o espaço, split vai quebrar a linha
except IndexError:
    pass #pass é colocado para bloco vazio
finally:
    arquivo.close()

if arquivo.closed:
    print('arquivo fechado')