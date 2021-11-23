#! python
class Humano:
    especie = 'Homo Sapiens' #atributo diretamente dentro da classe é um atributo de classe

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self): #metodo para leitura vai possibilitar fazer validacoes
        return self._idade
    
    def set_idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade


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
    jose = HomoSapiens('José')
    jose.set_idade(40)
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')

