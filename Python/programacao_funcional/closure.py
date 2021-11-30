def multiplicar(x): #funcao closure(escopo externo)
    def calcular(y):#(escopo interno)
        return x * y #a execução da função vai pegar o 'x'
    return calcular # vai retornar a função aninhada
    
if __name__=='__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print (dobro,triplo)

    print (f'O triplo de 3 é {triplo(3)}')
    print (f'O dobro de 7 é {dobro(7)}')