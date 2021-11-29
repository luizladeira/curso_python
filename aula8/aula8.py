"""
Entrada de dados - Aula 08
"""
import datetime

nome = input("Qual o seu nome? ")
data_agora = datetime.date.today()
ano_atual = data_agora.strftime("%Y")
ano_nascimento = input("Qual seu ano de nascimento? ")
idade_user = (int(ano_atual)-int(ano_nascimento))

print(f'{nome} tem {idade_user}')

"""
Soma utilizando input
"""

number_1 = int(input("Digite um número: "))
number_2 = input("Digite outro número: ")
number_2 = int(number_2)

print("A soma é:", number_1+number_2)