from datetime import datetime
from Desafio_POO import Cliente, Vendedor, Compra
from poo.Desafio_POO import cliente, vendedor

def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 4), 256)
    cliente.registra_compra(compra1)
    cliente.registra_compra(compra2)
    print (f'Cliente: {cliente}')