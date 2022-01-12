"""
Expressões Condicionais com operador OR
"""

nome = input('Qual o seu nome? ')
print(nome or 'Você não digitou nada')

# Exemplo 2
a = 0
b = None
c = False
d = []
e = {} # dicionario vazio
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel)