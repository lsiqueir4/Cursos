from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

# enquanto numero informado for diferente do num secreto
while numero_informado != numero_secreto:
    numero_informado = int(input("informe o numero:"))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
