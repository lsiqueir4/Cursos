# fibonacci com recursao

def fibonacci(quantidade, sequencia=(0, 1)):
    #Importante a condicao de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
    #tupla =(quantidade, sequencia +  soma dos dois ultimos valores
    
if __name__=='__main__':
    for fib in fibonacci(20):
        print(fib)