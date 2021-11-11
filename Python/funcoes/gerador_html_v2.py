# parametros nomeados
def tag_bloco(texto, classe='Success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</div>'

if __name__=='__main__':
    print(tag_bloco('bloco')) #outros parametros permanecem padrão
    print(tag_bloco('inline e classe', 'info', True)) #parametros por ordem
    print(tag_bloco('inline', inline=True)) #Parametros fora de ordem, necessário nomear