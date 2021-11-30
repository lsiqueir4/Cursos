compras = (
    {'quantidade': 2, 'preco' : 10},
    {'quantidade': 3, 'preco' : 20},
    {'quantidade': 5, 'preco' : 14}
)

def calc_preco_total(c): 
    return c['quantidade'] * c['preco']

#Defini uma funcao e executei ao invés de utilizar o lambda
totais = tuple(map( calc_preco_total, compras))

print('Precos totais:', totais)
print('Totais gerais:', sum(totais))