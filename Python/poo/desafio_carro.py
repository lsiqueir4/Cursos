velmax = 180

class Carro:
    def __init__(self, velmax, delta=5):
        self.velmax = velmax
        self.delta = delta
    def acelerar(delta=5):
        delta += delta
        return delta
    
    def frear(delta=5):
        delta -= delta
        return delta

    def limitar(delta):
        if delta >= velmax:
            delta == velmax
        elif delta <= 0:
            delta == 0  
             
        
if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))

