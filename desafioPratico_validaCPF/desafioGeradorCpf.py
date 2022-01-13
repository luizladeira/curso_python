"""
Utilizando a importação do modulo padrão RANDOM
"""
from random import randint

numero = str(randint(100000000, 999999999))  # convertendo para string
novo_cpf = numero
index_reverso = 10   # contador reverso
total = 0

for index in range(19):
    if index > 8:   # indice vai de 0 a 9
        index -= 9  # pegando os 9 primeiros digitos

    print(novo_cpf[index], index, index_reverso)
    total += int(novo_cpf[index]) * index_reverso  # ele guarda a multiplicação na variavel total

    index_reverso -= 1  # ele diminui o contador reverso
    if index_reverso < 2:  # se ele for menor que dois ele começa a formula da segunda coluna
        index_reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)

print(novo_cpf)

