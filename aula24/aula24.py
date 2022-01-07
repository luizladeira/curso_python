"""
Desempacotamento de Listas
"""
lista = ['Amanda', 'Felipe', 'Gilberto']

n1, n2, n3 = lista
print(n2)

# ERRO
print('\n Com erro: ')
print(n1, n2)


# Com *nome Ele gera outra lista com o restante dos valores para frente
lista_2 = ['Amanda', 'Felipe', 'Gilberto', 1, 2, 3, 4, 5]
n1, n2, n3, *outra_lista = lista_2
print('\n Com *nome Ele gera outra lista com o restante dos valores para frente: ')
print(outra_lista)


# PEGANDO O ULTIMO VALOR DA LISTA
lista_3 = ['Amanda', 'Felipe', 'Gilberto', 1, 2, 3, 4, 5]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista_3
print('\n PEGANDO O ULTIMO VALOR DA LISTA: ')
print(ultimo_da_lista)

# Exemplo 2 - PEGANDO O ULTIMO DA LISTA
lista_4 = ['Amanda', 'Felipe', 'Gilberto', 1, 2, 3, 4, 5, 6, 7, 8, 9]
*outra_lista_4,  ultimo_da_lista_4 = lista_4
print('\n Exemplo 2 - PEGANDO O ULTIMO DA LISTA ')
print(ultimo_da_lista_4)

# Exemplo 2 - PEGANDO O 3 ULTIMOS DA LISTA
lista_5 = ['Amanda', 'Felipe', 'Gilberto', 1, 2, 3, 4, 5, 6, 7, 8, 9]
*outra_lista_5,  N1, N2, N3 = lista_5
print('\n Exemplo 2 - PEGANDO O 3 ULTIMOS DA LISTA ')
print(outra_lista_5, N2)

# Exemplo 3 - Senão me importo com o restante da lista alem dos dois primeiros
lista_6 = ['Amanda', 'Felipe', 'Gilberto', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n3, *_ = lista_6  # *_ indica para outros desenvolvedores que nao irei utilizar o restante
print('\n Exemplo 3 - Senão me importo com o restante da lista alem dos dois primeiros: ')
print(n3)