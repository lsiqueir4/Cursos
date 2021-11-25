#! python
class Humano:
    especie = 'Homo Sapiens' #atributo diretamente dentro da classe é um atributo de classe

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property #decorator, vai acessar a função get como um atributo
    def idade(self): #metodo para leitura vai possibilitar fazer validacoes
        return self._idade

    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada')

    @idade.setter
    def idade(self, idade):
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

    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
    
    @property
    def inteligente(self):
        return True

if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    grogn = Neanderthal('Grogn')

    print('{} da classe {}, inteligente: {}'.format(jose.nome, jose.__class__.__name__, jose.inteligente))
    print('{} da classe {}, inteligente: {}'.format(grogn.nome, grogn.__class__.__name__, grogn.inteligente))

