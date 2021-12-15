"""
01)
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

import datetime

num1 = input("Digite um número? ")

if num1.isnumeric():
    result = int(num1) % 2
    if result == 0:
        print(f'O número {num1} é par')
    else:
        print(f'O número {num1} é impar')
else:
    print(f'O {num1} não é um número inteiro, por favor digite um número inteiro.')

"""
02)
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex.: Bom dia das 0h as 11h am 
     Boa tarde das 12h as 17h pm
     Boa Noite das 16 as 23h pm
"""

data_user = int(input("Digite a hora agora (0-23): "))
data_now = datetime.datetime.now()
horario_agora = int(data_now.strftime('%H'))

if (data_user >= 0 and data_user <= 11):
   print(f'Bom dia! {data_user}')
elif (data_user >= 12 and data_user <= 17):
   print("Boa Tarde!")
elif (data_user >= 18 and data_user <= 23):
   print("Boa Noite")
else:
   print("Foi nenhum horario kkkkk....")

"""
03)
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 a 6 letras, escreva "Seu nome é muito grande".
"""

primeiro_nome = input("Digite seu primeiro nome? ")
qtd_caracteres = len(primeiro_nome)

if qtd_caracteres <= 4:
    print(f'Seu nome é curto e possui {qtd_caracteres} caracteres... ')
elif qtd_caracteres >= 5:
    print(f'Seu nome é grande e possui {qtd_caracteres} caracteres...')
else:
    print(f'Tudo certo!!!! Seu nome contém {qtd_caracteres}')
