class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__():
        return (f'nome: {self.nome} idade:{self.idade}')

    def isAdult():

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Cliente(Pessoa):
    def __init__(self, nome, idade, compras = [0]):
        super().__init__(nome, idade)
        self.compras = compras

    def registra_compra(Compra):
    
    def get_data_ultima_compra():

    def total_compras():


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor



