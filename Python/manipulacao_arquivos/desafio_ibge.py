import csv

separador = ','
with open('desafio-ibge.csv'.encode(encoding = 'iso-8859-1')) as entrada:
    for linha, conteudo in enumerate(entrada):
        if linha:
            colunas = conteudo.strip().split(separador) #define cada coluna
            print (f'Campo 9:{colunas[8]} Campo 4:{colunas[3]}') #indice começa em 0

        