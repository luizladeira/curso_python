"""
Enumerate - Enumerar elementos da lista #list
OBS.: Enumerate simplesmente enumera os indices de uma lista
"""
lista = [
    ['Edu', 'Monica', 'João'],
    ['Maria', 'José'],
    ['Gustavo', 'Otávio', 'Luiz', 'Nancy']
]

enumerada = enumerate(lista)
print('Enumerate', enumerada, '\n')
lista_enumerada = list(enumerada)
print('Conversão de Enumerate para Lista', lista_enumerada)  # Convertido o tipo enumerate para Lista, não posso adicionar e nem remover o que possui dentro da tupla

"""
Exemplificação:

    [ <-- ENUMERATE
                 Indice: 0 | Indice: 1   
      Tupla 0 -  (0,        ['Edu', 'Monica', 'João']), 
      Tupla 1 -  (1,        ['Maria', 'José']), 
      Tupla 2 -  (2,        ['Gustavo', 'Otávio', 'Luiz', 'Nancy'])
    ]
    
"""

print(lista_enumerada[2][1])

for v1, v2 in enumerate(lista, 63):
    print('Indice: ', v1, ' | Valor -> ', v2)

print("\n DESEMPACOTAMENTO EXEMPLO: ")
for v1 in enumerate(lista, 63):
    valor_enumerado, minha_lista = v1
    print(valor_enumerado, minha_lista)
