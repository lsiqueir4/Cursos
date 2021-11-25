#! python

from abc import ABCMeta


class Animal:
    @property
    def capacidades(self):
        return ('dormir','comer','beber' )

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar','falar','estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes') 

class SpiderMan(Aranha, Homem): #herança multipla, herda das duas classes
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias entre predios')

if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')
    aranha = Aranha()
    print(f'aranha: {aranha.capacidades}')
    peter = SpiderMan()
    print (f'peter: {peter.capacidades}')