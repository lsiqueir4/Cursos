pessoas = [
    {'nome': 'Pedro' , 'idade': 11},
    {'nome': 'Mariana' , 'idade': 18},
    {'nome': 'Arthur' , 'idade': 26},
    {'nome': 'Rebeca' , 'idade': 6},
    {'nome': 'Tiago' , 'idade': 19},
    {'nome': 'Gabriela' , 'idade': 17}
]

menores = filter(lambda p: p['idade'] < 18, pessoas) # filtrando pessoas com idade < 18

filtronome = filter(lambda p: len(p['nome']) >= 7, pessoas) #filtrando pessoas com nome maior q 7
print(list(menores))

print(list(filtronome))