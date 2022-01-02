"""
FUNÇÕES: Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista    # str
* Enumerate - Enumerar elementos da lista # list para objetos iteraveis
"""

# FUNÇÃO SPLIT
var_string = "O Brasil é o país do Futebol, o Brasil é pentacampeão."
lista_split_1 = var_string.split(' ')
print(lista_split_1, '\n')

lista_split_2 = var_string.split(',')
print(lista_split_2, '\n')

# iterando a lista 1
print(f'ITERANDO LISTA 1')

palavra = ''
contagem = 0

for valor in lista_split_1:
    print(f'A palavra {valor} - apareceu {lista_split_1.count(valor)}x vezes \n')
    quantidade_vezes = lista_split_1.count(valor)

    if quantidade_vezes > contagem:
        contagem = quantidade_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes {palavra} foi ({contagem}x)')

# LISTA 2 - strip tira os espaços e capitalize como o inicio maiusculo
print('\nLISTA 2 - strip tira os espaços e capitalize como o inicio maiusculo')
for valor in lista_split_2:
     print(valor.strip().capitalize())

# FUNÇÃO JOIN - é utilizado para transformar uma lista em uma string
print(f'\nLISTA:  {lista_split_1}')
string_listas = ",".join(lista_split_1)
print(string_listas, '\n')

# FUNÇÃO ENUMERATE
for indice, valor_real in enumerate(lista_split_1):
    print(indice,'-', valor_real, lista_split_1[indice])

# uma lista pode conter outras listas
listas_array = [
    [1, 2],
    [3, 4],
    [5, 6, 7]
]
print(listas_array)
for v in listas_array:
    print(v[0])

# Exemplo 2
print('\n UTILIZANDO VARIAS LISTA SEM ENUMERATE')
listas_array_2 = [
    [0, "Luiz"],
    [1, "Bruno"],
    [2, "Nancy"]
]
print(listas_array_2)
for indice_2, nome in listas_array_2: # FAZ O MESMO QUE A ENUMERATE REALIZA DE FORMA SIMPLIFICADA
    print(indice_2, nome)

print('\n UTILIZANDO COM ENUMERATE')
listas_array_3 = ['A', 'B', 'C']
for indice_3, nome_3 in enumerate(listas_array_3):  # DESEMPACOTAMENTO
        print(indice_3, nome_3)