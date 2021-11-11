#packing
def soma_n(*numeros): #empacotamento, vai permitir colocar quantos parametros forem necessarios
    soma=0
    for n in numeros: #realiza a soma dos parametros inseridos
        soma += n
    return soma

if __name__ =='__main__':
    print (soma_n(1, 1, 1, 1, 1, 1, 1))

#unpacking
nums = (1,2,3)
print (soma_n(*nums)) #desempacota os parametros da tupla inserindo como parametros na função