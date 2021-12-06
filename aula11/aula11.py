"""
FUNÇÃO len - quantidade de caracteres e nao funciona com numeros

"""
#EXEMPLO 1
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres <= 3:
    print('Você precisa digital pelo 2 caracteres')
else:
    print('Tudo CERTO!!!!!')

#EXEMPLO 2

string1 = input('Digite um valor: ')
string2 = input('Digite outro valor: ')
print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
