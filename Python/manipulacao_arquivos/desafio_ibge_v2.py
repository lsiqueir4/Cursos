import csv
from urllib import request

def read(url):
    with request.request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1') #decode do ISO-8859-1
        print('Download Completo!')
        for cidade in csv.reader(dados.splitlines()): #.splitlines separa a linha em virgulas
            print(f'{cidade[8]} : {cidade[3]}') #busca as linhas pelo indice, lembrando que começa por 0

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv') #r =  raw para nao interpretar codigo na string