"""
 FOR
 Interando Strings com FOR
 Função range(start=0, stop, step=1)
"""
texto = "Python"

for letra in texto:
    print(letra)

# Contador no for com enumerate
print("\n Contador com enumerate: ")
for n, letra in enumerate(texto):
    print(n, letra)

# For com range
print("\n FOR com função range: ")
for n in range(3, 43, 2):
    print(n)

# ACHANDO MULTIPLOS
print('\n ACHANDO MULTIPLOS DE 8:')
for n in range(200):
    if n % 8 == 0:
        print(f'{n} é multiplo de 8')

#
texto = 'Python'
new_string = ''

for letra in texto:
    if letra == 't':
        new_string = new_string + letra.upper()
    elif letra == 'n':
        new_string += letra.upper()
    else:
        new_string += letra
print(new_string)

"""
    Utilizando continue e break
        continue - pula para o proximo laço
        break - para o laço
"""
texto_dois = 'Python'
new_string_dois = ''

for letra_dois in texto_dois:
    if letra_dois == 't':
        continue
        new_string_dois = new_string + letra_dois.upper()
    elif letra_dois == 'n':
        break
        new_string_dois += letra_dois.upper()
    else:
        new_string_dois += letra_dois
print(new_string_dois)
