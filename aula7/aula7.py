"""
Strings - Formatação
"""

nome = 'Luiz'
sobrenome = 'Ladeira'
idade = 31
altura = 1.63
e_maior = idade > 18
peso = 62.00
imc = peso/(altura*altura)

print(nome+" "+sobrenome, "tem", idade, "anos e seu IMC é", imc, "kg/m2")

# utilizando fstring de formatação
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f} kg/m2')
print("{} tem {} anos de idade e seu IMC é {:.2f} kg/m2".format(nome, idade, imc))
print("{0} tem {1} anos e seu IMC é {2}".format(nome, idade, imc))

# paramentros nomeados
print("{n} tem {i} anos e seu IMC é {im:.2f} kg/m2".format(n=nome+" "+sobrenome, i=idade, im=imc))