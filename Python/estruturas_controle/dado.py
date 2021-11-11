#Funcao sortear_dado numeros 1 a 6
#For com range 1 a 6
#Se for impar continue
#Se for par e for igual ao valor sorteado pela funcao dado imprimir string "ACERTOU"
#e depois chamar break
#se nao acertar chama o else.."NAO ACERTOU"

from random import randint

def sortear_dado():
    return randint(1 , 6) #no randint o 6 tbm vai entrar

for i in range(1 , 7):
    if i % 2 == 1: #Vai pular os impares
        continue
    if sortear_dado() == i:
        print (f"Acertou! Numero:{i}")
        break #se executa o break nao chama o else
else: 
    print(f"Nao acertou o numero! Numero:{i}")

