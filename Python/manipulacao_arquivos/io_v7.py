import csv
#msm processo fazendo o import da biblioteca csv, bem mais simples
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print ('Nome: {}, Idade: {}'.format(*pessoa))
