def fibonacci(sequencia=[0,1]):
    #uso de mutaveis como valor default(ARMADILHA!)
    sequencia.append(sequencia[-1] +sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print (fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))


#[0, 1, 1] 1712179859912  - O ID é o mesmo, ou seja, o script alterou o valor da funcao criada ao inves de criar um novo
#[0, 1, 1, 2]
#[0, 1, 1, 2, 3] 1712179859912