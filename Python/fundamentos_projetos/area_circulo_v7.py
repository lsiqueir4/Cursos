#! python
import math #importa math
from math import pi #importa apenas o pi

def circulo(raio):
    return (pi * float(raio)) ** 2

if __name__ == '__main__':
    raio = input('Informe o raio:')
    area = circulo(raio)
