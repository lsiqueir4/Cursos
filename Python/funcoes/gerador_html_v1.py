def tag_bloco(texto, classe='Success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__=='__main__':
    #Testes(Assertions)
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="Success">Incluido com sucesso!</div>'
