"""
Variáveis

Iniciar com letra, pode conter números, separar _, letras minúsculas

"""

nome = 'Luiz'
sobrenome = 'Ladeira'
idade = 31
altura = 1.63
e_maior = idade > 18
peso = 62.00
imc = peso//(altura*altura)

print("Nome:", nome+" "+sobrenome)
print("Idade:", idade)
print("Altura:", altura)
print("É maior?", e_maior)

print(nome+" "+sobrenome, "tem", idade, "anos e seu IMC é", imc, "kg/m2")