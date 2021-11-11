#! python
import math #importa math
from math import pi #importa apenas o pi
import sys


def circulo(raio):
    return (pi * float(raio)) ** 2


def help():
    print (f"""\
             É necessário informar o raio do cículo. 
             Sintaxe: {sys.argv[0][2:]} <raio>""") #sys.argv[0] puxa o nome do arquivo, [2:] pega a string a partir do 3 caracter (0,1,2)


if __name__ == '__main__':
    if len(sys.argv) < 2: #se o tiver menos de 2 argumentos...
        help ()
        sys.exit(1) #sai do script = errno.EPERM
    elif not sys.argv[1].isnumeric():
        help ()
        print("O raio deve ser um valor numerico")
        sys.exit(2) # = errno.EINVAL
    else:
        raio = sys.argv[1] #argumento passado no terminal = raio
        area = circulo(raio)
        print ('Area do Circulo' , area)
