velmax = 180

class Carro:
    def __init__(self, velmax):
        self.velmax = velmax
        self.velatual = 0

    def acelerar(self, delta=5):
        maxima = self.velmax
        nova = self.velatual + delta
        self.velatual = nova if nova <= maxima else maxima
        return self.velatual
    
    def frear(self, delta=5):
        nova = self.velatual - delta
        self.velatual = nova if nova>= 0 else 0
        return self.velatual

   
if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))

