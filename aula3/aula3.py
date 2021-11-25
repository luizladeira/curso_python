"""
TIPOS DE DADOS

str - string
int - inteiro
float - flutuante
bool - booleano/logico
"""

print(type(False))
print('LUIZ', type('LUIZ'))
print(10, type(10))
print(0, type(0))
print('L' == 'l', type('L' == 'l'))
print(bool(0))
print('LUIZ', type('LUIZ'), bool('LUIZ'))
print('10', type('10'), type(int('10'))) #conversao de tipo de variavel para inteiro

#ATIVIDADE

#STRING NOME
print('Luiz',type('Luiz'))

#IDADE: INT
print('31',type(int('31')))

#ALTURA: FLOAT
print('1.63',type(float('1.63')))

#MAIOR DE IDADE
print('10' > '18', type(int('10' > '18')))



a = 2
b = 9

if(a > b):
    print(a,' é maior que ',b)
else:
    print(a,' é menor que ',b)