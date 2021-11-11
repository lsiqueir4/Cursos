#! python
import math #importa math
from math import pi #importa apenas o pi

def circulo(raio):
    area = (pi * float(raio)) ** 2
    print ('Area do circulo', area)

if __name__ == '__main__':
    raio = input('Informe o raio:')
    circulo(raio)
