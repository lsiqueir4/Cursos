def get_tipo_dia(dia): 
    dias = {
        1: 'Fim de semana',
        2: 'Semana',
        3: 'Semana',
        4: 'Semana',
        5: 'Semana',
        6: 'Semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '**INVALIDO**')

if __name__ == '__main__':
    for dia in range(12):
        print (f'{dia}: {get_tipo_dia(dia)}')

