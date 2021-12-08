from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94) #TUPLA, VALORES SAO IMUTAVEIS

print (sorted(valores)) #função imutavel, os valores não foram alterados na lista

valores.sort() #função mutavel, a função alterou a lista

print(valores)

#funções imutaveis
print(min(valores)) #menor valor
print(max(valores)) #maior valor
print(sum(valores)) #soma dos valores
print(reduce(add, valores)) #adiciona todos os valores usando o reduce(mesmo resultado da soma)
print(list(reversed(valores)))