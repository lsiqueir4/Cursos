MaiorIdade = 18

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'Nome: {self.nome} Idade: {self.idade}'

    def isAdult(self):
        return (self.idade or 0) > MaiorIdade
