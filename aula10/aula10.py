"""
Operadores Relacionais
        == igualdade
        > maior que
        >= maior que ou igual a
        < menor que
        <= menor que ou igual a
        != diferente
"""

print(2 == 2)

num_1 = 2
num_2 = 2

expressao = (num_1 > num_2)
print(expressao)

expressao = (num_1 >= num_2)
print(expressao)

expressao = (num_1 <= num_2)
print(expressao)

expressao = (num_1 != num_2)
print(expressao)

nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")
idade = int(idade)

#idade limite para pegar emprestimo
idade_limite = 18

idade_menor = 20
idade_maior = 30

if(idade >= idade_limite):
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')

if(idade >= idade_menor and idade <= idade_maior):
    print(f'{nome} pode pegar o empréstimo, pois está na faixa etária de idade < 30 e > 20')
else:
    print(f'{nome} não pode pegar o empréstimo, pois está fora da faixa etária de idade < 30 e > 20')