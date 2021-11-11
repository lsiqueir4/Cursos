produto = {'nome': 'Caneta Chic', 'preco': 14.99, 
           'importada': True, 'estoque': 793}

for chave in produto: #ou produto.keys, é a msm coisa
    print(chave) #imprimira as chaves

for valor in produto.values(): #vai imprimir os valores
    print(valor)

for chave, valor in produto.items (): #pega a chave e o valor
    print(chave, '=', valor)