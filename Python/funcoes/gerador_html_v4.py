# parametros nomeados
def tag_bloco(conteudo,*args, classe='Success', inline=False): #args gera uma tupla
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</div>'

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens) #join fara uma concatenação na string inicialmente vazia
    return f'<ul>{lista}</ul>'

if __name__=='__main__':
    print(tag_bloco('bloco')) #outros parametros permanecem padrão
    print(tag_bloco('inline e classe', 'info', True)) #parametros por ordem
    print(tag_bloco('inline', inline=True)) #Parametros fora de ordem, necessário nomear
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'sabado', 'domingo', classe='info', inline=True))