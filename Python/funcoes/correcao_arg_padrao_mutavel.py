def fibonacci(sequencia=None):
    sequencia = sequencia or [0,1] #Se sequencia for none, vai adotar [0,1]
    sequencia.append(sequencia[-1] +sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print (fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))


#[0, 1, 1] 2033112404424
#[0, 1, 1, 2]
#[0, 1, 1] 2033112404936