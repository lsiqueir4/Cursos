#! python
class Humano:
    especie = 'Homo Sapiens' #atributo diretamente dentro da classe é um atributo de classe

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        