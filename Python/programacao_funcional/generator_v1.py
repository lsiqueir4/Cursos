def cores_arco_iris(): #cada execução da função vai retornar um yield
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'

if __name__ == '__main__':
    generator = cores_arco_iris()
    while True:
        print(next(generator))