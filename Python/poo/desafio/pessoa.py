MaiorIdade = 18

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__():
        if not self.idade:
            return self.nome
        return f'Nome: {self.nome} Idade: {self.idade}'

    def isAdult(self):
        return True if self.idade >= MaiorIdade