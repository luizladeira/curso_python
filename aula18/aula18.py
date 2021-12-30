"""
 Iterando Strings com While
 Índices
 0123456789.......33
"""
# EXEMPLO 1
frase = "o rato roeu o roupa do rei de roma"
tamanho_frase = len(frase)
print(f'Tamanho da Frase: {tamanho_frase}\n')
contador = 0
new_string = ''

while contador < tamanho_frase:
    print(f'Letra: [{frase[contador]}]', f' -> Indice: [{contador}] \n')
    letra = frase[contador]
    new_string += frase[contador]  # concatenar
    print(new_string)
    contador += 1

print(f'Nova String: {new_string}')

# EXEMPLO 2

frase_dois = "o rato roeu o roupa do rei de roma"
tamanho_frase_dois = len(frase_dois)
contador_dois = 0
new_string_dois = ''
input_usuario = input('Qual letra deseja colocar Maíuscula? ')

while contador_dois < tamanho_frase_dois:
    letra_dois = frase[contador_dois]
    if letra_dois == input_usuario:
        new_string_dois += input_usuario.upper() #converte a letra para maiuscula
    else:
        new_string_dois += letra_dois
    contador_dois += 1

print(f'Nova String: {new_string_dois}')

