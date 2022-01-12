"""
Operador Ternário
"""
# SEM OPERADOR TERNÁRIO
logged_user = False

if logged_user:
    msg = 'Usuário Logado'
else:
    msg = 'Usuário necessita estar logado'

print(msg)

# UTILIZANDO OPERADOR TERNÁRIO
logged_user = True
msg = 'Usuario Logado.' if logged_user else 'Usuário necessita estar logado'
print(msg)

# Exemplo 2
idade = input('Digite qual sua idade: ')
if not idade.isnumeric():
    print('Você necessita digitar números inteiros: ')
else:
    idade = int(idade)
    e_maior_de_idade = (idade >= 18)
    mensagem = 'Pode acessar' if e_maior_de_idade else 'Não pode acessar'
print(mensagem)