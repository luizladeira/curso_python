"""
VALIDADOR DE CPF
CPF: 168.995.350-09
---------------------------------------------------
1 * 10 = 10                #  1 * 11 = 11
6 * 9 = 54                 #  6 * 10 = 60
8 * 8 = 64                 #  8 * 9 = 72
9 * 7 = 63                 #  9 * 8 = 72
9 * 6 = 54                 #  9 * 7 = 63
5 * 5 = 25                 #  5 * 6 = 30
3 * 4 = 12                 #  3 * 5 = 15
5 * 3 = 15                 #  5 * 4 = 20
0 * 2 = 0                  #  0 * 3 = 0
                           #->  0 * 2 = 0
        297                #         343
11 - (297 % 11) = 11       #    11 - (343 % 11) = 9
11 > 9 = 0                 #
DIGITO 1 = 0               # DIGITO 2 = 9

"""

while True:
    cpf = input('Digite o seu CPF: ')
    #cpf = '16899535009'
    novo_cpf = cpf[:-2]  # retira os dois ultimos digitos
    index_reverso = 10   # contador reverso
    total = 0

    for index in range(19):
        if index > 8:   # indice vai de 0 a 9
            index -= 9  # pegando os 9 primeiros digitos

        print(cpf[index], index, index_reverso)
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
    if cpf == novo_cpf:
        print(f'Seu CPF é Válido {cpf}')
    else:
        print(f'Seu CPF é inválido {cpf}')
