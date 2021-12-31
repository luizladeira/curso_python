# CRIANDO UM JOGO DE ADVINHAÇÃO COM LAÇOS E
print("JOGO DE ADIVINHAÇÃO: \n")
palavra_secreta = "perfume"
digitada = []  #criando uma lista vazia
total_de_chances = 3

while True:
    if total_de_chances <= 0:
        print('Você perdeu!!')
        break
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ahh isso vale, digite apenas uma letra: ")
        continue

    digitada.append(letra)
    print(digitada)

    if letra in palavra_secreta:
        print(f'uHulll, a Letra "{letra}" existe na palavra....\n')
    else:
        print(f'Aff, a letra "{letra}" a letra não existe na palavra secreta.. \n')
        digitada.pop() #exclui a ultima palavra digitada

    palavra_secreta_temporaria = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitada:
            palavra_secreta_temporaria += letra_secreta
        else:
            palavra_secreta_temporaria += "*"

    if palavra_secreta_temporaria == palavra_secreta:
        print(f'BOAAAA, você GANHOUUUUUU!!!! A palavra era {palavra_secreta_temporaria} \n')
        break
    else:
        print(f'A palavra secreta está assim: ', palavra_secreta_temporaria, '\n')

    if letra not in palavra_secreta:
        total_de_chances -= 1

    print(f'Você ainda tem {total_de_chances} chances para jogar!\n')
