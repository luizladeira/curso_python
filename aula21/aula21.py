"""
    F0R / ELSE
"""
lista = ['Luiz', 'João', 'bruno']

for valor in lista:
    print(valor)
    continue
    print(valor)  # não é executado por conta do continue


for valor in lista:
    print(valor)
    break
    print(valor)  # não é executado porque ele saiu quando passou no break


# USANDO startswith [começa com a letra definida]
# Exemplo 1
for valor in lista:
    if valor.startswith('b'):  # checa que se o valor da string VALOR se ela começa com a determinada letra dentro do ()
        print("Começa com b de", valor)
    else:
        print("Não começa com b, pois o nome é: ", valor)


# USANDO lower() = ele converte para minusculo se for maiusculo e maiusculo para minusculo
comeca_com_j = False
for valor in lista:
    if valor.lower().startswith('l'):
        comeca_com_j = True
        print("Existe uma palavra que começa com L de ", valor)
        break
else:
    print("Não existe uma palavra que começa com L")

