def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params) #**params = os parametros precisarao ser nomeados, * tupla ** dicionario

def imposto_x(importado):
    return 0.22 if importado else 0.13

def imposto_y(explosivo, fator_multi=1):
    return 0.11 * fator_multi if explosivo else 0

if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True) 
    #os parametros precisam ser nomeados, se forem chamados por posicao vai dar erro
    preco_final = calc_preco_final(preco_final, imposto_y, explosivo=True,fator_multi= 1.5) 
    print (f'PRECO FINAL R$ {preco_final}')