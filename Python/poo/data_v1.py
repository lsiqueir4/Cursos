class Data: #Classe se define com 1 letra maiuscula
    def __init__(self, dia, mes, ano): #criando os atributos(construtor)
        self.dia= dia
        self.mes=mes
        self.ano=ano
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}' #self = obj atual

d1 = Data(5,12,2019)
print (d1)

d2 = Data(7,12,2020)
print (d2)