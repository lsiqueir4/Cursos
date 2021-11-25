class ClasseSimples:
    contador = 0

    def __init__(self):
        self.contar() #na inicialização da classe chama o metodo de contar
 
    @classmethod #metodo de classe, a propria classe é a entrada
    def contar(cls):
        cls.contador += 1

if __name__ =='__main__':
    lista  = [ClasseSimples(), ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador) #esperado 4