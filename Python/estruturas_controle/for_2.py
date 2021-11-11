palavra = 'paralelepipedo'

for letra in palavra:
    print (letra, end=',') #end=',' fara imprimir na mesma linha (padrao \n = quebra de linha)

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print (nome)
for posicao, nome in enumerate(aprovados):
    print (posicao +1, nome)

dias_semana = ('Domingo', 'Segunda', 'Terca', 
               'Quarta', 'Quinta')
for dia in dias_semana:
    print(f'HJ É {dia}')

for letra in set('muito legal'):
    print (letra, end=',')