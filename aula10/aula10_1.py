"""
Operadores Lógicos
        AND
        OR
        NOT
        IN
        NOT IN
"""

"""
NOT
"""

b = 21
a = 5

#EXEMPLO 1
if not b > a:
    print('B é maior que A')
else:
    print('A é maior do que B')

# EXEMPLO 1
x = ''
y = 1

if not x:
    print('Por favor, preencha o valor de B')

"""
IN
"""
# exemplo 01
nome = 'Luiz'
if 'u' in nome:
    print(f'Existe a letra u no seu {nome}')
else:
    print('Não existe')

# exemplo 02

if 'adeira' not in nome:
    print('Existei')
else:
    print("Existe o texto adeira")

#EXEMPLO 2

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_db = 'luiz'
senha_db = '2345'

if usuario_db == usuario and senha_db == senha:
    print('Você está logado no sistema')
else:
    print('Usuário e senha inválidos....')
