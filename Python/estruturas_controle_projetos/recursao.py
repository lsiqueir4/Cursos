def imprimir (maximo, atual):
    #prestar atencao na condicao de parada
    if atual < maximo:
        print(atual)
        imprimir (maximo, atual +1)

imprimir(1000, 1)