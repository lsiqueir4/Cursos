def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:])) # -2: vai pegar os dois ultimos resultados
        if len(resultado) == quantidade: #len = tamanho do array, quantidade de elementos na sequencia
            break 
        return resultado

if __name__ == '__main__':
    for fib in fibonacci(10):
        print (fib)
