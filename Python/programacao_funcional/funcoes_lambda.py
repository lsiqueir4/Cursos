compras = (
    {'quantidade': 2, 'preco' : 10},
    {'quantidade': 3, 'preco' : 20},
    {'quantidade': 5, 'preco' : 14}
)

totais = tuple(
    map( #o map vai calcular a funcao de lambda e gerar uma nova tupla, sem alterar a anterior
        lambda compra: compra['quantidade'] * compra['preco'], #funcao lambda(anonima)
        compras #a segunda variavel é a tupla com quem quero trabalhar

    )
)

print('Precos totais:', totais)
print('Totais gerais:', sum(totais))