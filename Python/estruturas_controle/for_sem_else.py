PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'Joao gosta de futebol e política',
    'a praia foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print ('TEXTO POSSUI PALAVRA PROIBIDA:', palavra)
            found = True
            break

    if not found:
        print('TEXTO OK:', texto)