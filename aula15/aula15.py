"""
    MANIPULANDO STRINGS - AULA 15

    * String indices
    * Fatiamento de strings [inicio:fim:passo]
    * Funções built-in len, abs, type, print, etc ...
    Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
    https://docs.python.org/3/library/stdtypes.html (tipos built-in
    https://docs.python.org/3/library/functions.html (funções built-in)
"""
# String indices
# indices POSITIVOS [012...]
texto = 'Python <3'
print(texto[3])
print(texto[7])

# String indices
# String indices NEGATIVOS -[98765...]
texto_2 = 'Python <3'
print(texto_2[-7:-2])

# Fatiamento de strings [inicio:fim:passo]
url = 'www.luizladeira.com/'
print(url[:1])   #retiro o ultimo caracter da string
print(url[4:15]) #começo do 4 caracter vou até a 15 caracter
print(url[:8])
print(texto_2[7:])
print(texto_2[0:6:2]) #ele pega a string no tamanho de 0 a 6 e pega um e pulo outro
print(texto_2[0::2]) #ele pega a string do tamanho total e pega um e pulo um

# Funções built-in len
texto_3 = "Luiz Paulo"
print(len(texto_3)) #conta caracteres da string


