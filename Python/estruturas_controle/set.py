PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'Joao gosta de futebol e política',
    'a praia foi divertida'
]

for texto in textos:
    intersecao= PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('TEXTO POSSUI PALAVRAS PROIBIDAS:', intersecao)
    else:
        print('TEXTO OK:', texto)