"""
    Listas
    Fatiamento
    append, insert, pop, del, clear, extend, +
    min, max
    range
"""
# STRING só suporta um unico valor
print("\n STRINGS: ")
string = 'ABCDE'
print(string[-1])

# Lista com vários valores - exemplo: lista = [1, 2, 3, 4, "String", True, 10.5]
print("\n LISTA COM VÁRIOS VALORES: ")
lista = ['A', 'Banana', 'C', 'D', 'E', 10.4]  # Indices = 0,1,2,3,4 podendo ser negativos também
print(lista[-1])
print(lista)

# Modificando os valores da lista
print("\n MODIFICANDO OS VALORES DA LISTA: ")
print(lista[5])
lista[5] = 'Qualquer outra coisa'
print(lista[5])

# Fatiamento
print("\n FATIAMENTO: ")
print(lista[0:3])
print("DE 0 A 3: ", lista[:3])
print("INICIA NO INDICE 2 ATÉ O FINAL: ", lista[2:])
print("ULTIMO LISTA DA MINHA LISTA ", lista[-1])
print("PULANDO DE DOIS EM DOIS ", lista[::2])
print("MOSTRANDO DE FORMA INVERTIDA ", lista[::-1])

# LISTA
print("\n LISTA: ")
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_2 = [9, 10, 11]
print(lista_1)
print(lista_2)

lista_3 = lista_1 + lista_2
print("JUNÇÃO DA LISTA 1 E LISTA 2:", lista_3, '\n')

# UTILIZANDO:  append, insert, pop, del, clear, extend, +
lista_1.extend(lista_2)
print("FUNÇÃO EXTENDS", lista_1, '\n')

lista_2.append('INSERÇÃO APPEND')
print("ADICIONANDO COM APPEND NO FINAL DA LISTA:", lista_2, '\n')

lista_2.insert(0, 'IN')
print("ADICIONANDO COM APPEND NO INICIO DA LISTA:", lista_2, '\n')

lista_2.pop()
print("DELETANDO COM POP NO FINAL DA LISTA:", lista_2, '\n')

lista_2.pop(1)
print("DELETANDO COM POP POR INDICE DA LISTA:", lista_2, '\n')

del(lista_1[2:5])
print("DELETANDO COM DEL POR FATIAMENTO:", lista_1, '\n')

# UTILIZANDO min, max
print("PEGANDO O MAIOR VALOR DA LISTA:", max(lista_1), '\n')
print("PEGANDO O MENOR VALOR DA LISTA:", min(lista_1), '\n')

# UTILIZANDO range
lista_4 = range(1, 10)
print("RANGE: ", lista_4, '\n')

#FUNÇÃO LIST
lista_4 = list(range(1, 10))
print("Objeto Interavel RANGE", lista_4, '\n')

# PEGAR DE 0 A 100 OS MUTIPLOS DE 8
lista_4 = list(range(0, 100, 8))
print("PEGAR DE 0 A 100 OS MULTIPLOS DE 8:", lista_4, '\n')

# UTILIZANDO O LAÇO FOR
print("UTILIZANDO O LAÇO FOR EM LISTAS: \n")
lista_4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0

for valor in lista_4:
    soma = soma + valor
    print("Interando a lista: ", soma, '\n')

# UTILIZANDO O LAÇO FOR PARA PEGAR O TIPO DE DADO NA LISTA
print("UTILIZANDO O LAÇO FOR PARA PEGAR O TIPO DE DADO NA LISTA: \n")
lista_4 = ['STRING', True, 10, -20, 10.2]
for elemento in lista_4:
    print(f'Tipo de elemento é {type(elemento)} e seu valor é {elemento} ')


