#! python
class Humano:
    especie = 'Homo Sapiens' #atributo diretamente dentro da classe é um atributo de classe

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        
if __name__ == '__main__':
    jose = Humano('Jose')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print (f'Humano.especia: {Humano.especie}')
    print (f'jose.especie: {jose.especie}')
    print (f'grokn.especie: {grokn.especie}')
