#! python
class Humano:
    especie = 'Homo Sapiens' #atributo diretamente dentro da classe é um atributo de classe

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
    
    @staticmethod #metodo estatico
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis' , 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod #metodo de classe
    def is_evoluido(cls): #função recebe a classe como parâmetro(polimorfismo)
        return cls.especie == cls.especies() [-1]
        
class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == '__main__':
    jose = Humano('Jose')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print (f'Humano.especia: {Humano.especie}')
    print (f'jose.especie: {jose.especie}')
    print (f'grokn.especie: {grokn.especie}')
    print (f'Neanderthal é evoluido? {Neanderthal.is_evoluido()}')
    print (f'Sapiens é evoluido? {HomoSapiens.is_evoluido()}')
