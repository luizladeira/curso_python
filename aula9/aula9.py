"""
Condições
        IF
        ELSIF
        ELSE
"""

#python utliza na hierarquia com 4 espaçoos

"""
if False:
    print("Verdadeiro")
    
print('A minha expressão não é verdadeira"')
"""

"""
if False:
    print("Verdadeiro")
else:
    print('A minha expressão não é verdadeira"')
"""

# ELIF - é apreviação de elseif
if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro")
    num1 = 2
    num2 = 4
    print(f"A soma é: {num1+num2}")
elif True:
    print("Mais uma verdadeiro")
    nome = input("Qual o seu nome? ")
    print(f"Seu nome é: {nome}")
else:
    print("A minha expressão não é verdadeira")
    idade = input("Olá, diga o sua idade? ")
    print(f"Sua idade é: {idade}")