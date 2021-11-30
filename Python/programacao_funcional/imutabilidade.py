from calendar import calendar, mdays, month_name #mdays = qtd de dias no mes, month_name = nome dos meses
from locale import setlocale, LC_ALL #localização de linguagem
from functools import reduce

#localizando para ptbr
setlocale(LC_ALL, "pt_BR")

#1 - pegar os indices de todos os meses com 31 dias
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1,13))
#2.(map) transformar os indices em nome
meses_nomes = map(lambda mes: month_name[mes], meses_31)
#3.(reduce) juntar tudo para imprimir
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nomes, 'Meses com 31 dias:')

print(meses_31)
print(juntar_meses)
