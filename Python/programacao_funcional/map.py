lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)#estrutura => lambda parametro: funcao, atributo
print(list(dobro))

lista_2 = [
    {'nome' : 'Joao', 'idade' : 31},
    {'nome' : 'Maria', 'idade' : 37},
    {'nome' : 'Jose', 'idade' : 26}
]

frase = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos', lista_2)

print(list(frase))

