"""
    Laços de repetição - while
    utilizado para realizar ações enquanto uma condição for verdadeira
"""

#WHILE
print('|||WHILE Simples|||')
x = 1
while x <= 100:
    print(x)
    x = x + 1
print('ACABOUUUUUUUUUUU')

#WHILE com continue
print('\n\n |||WHILE com continue|||')
x = 1
while x < 10:
    if x == 6:
        x = x + 1
        print(f'Esse não é para mostrar [{x}]')
        continue  # ele pula quando estiver o continue

    print(x)
    x = x + 1
print('ACABOUUUUUUUUUUU')

#WHILE com break
print('\n\n |||| WHILE 2 com break |||')
x = 1
while x < 10:
    if x == 4:
        x = x + 1
        print(f'Esse não é para mostrar [{x}]')
        break  # ele interrompe o laço de repetição pula quando estiver o continue

    print(x)
    x = x + 1
print('ACABOUUUUUUUUUUU')

#WHILE EXEMPLO
print('\n\n |||| WHILE EXEMPLO |||')
x = 0   #coluna
y = 0   #linha

while x < 10:
    y = 0
    while y <= 5:
        print(f'({x}),({y})')
        y += 1
    x += 1  # x = x+1
print("ACABOUUUUUU")


#WHILE EXEMPLO
print('\n\n |||| EXEMPLO CALCULADORA |||')

while True:
        number_1 = input("Digite um Número: ")
        number_2 = input("Digite outro Número: ")
        operador = input("Digite um operador ou sair: ")

        if not number_1.isnumeric() or not number_2.isnumeric():
            print("Você precisar digitar um Número")
            continue

        number_1 = int(number_1)
        number_2 = int(number_2)

        if operador == "+":
            print(number_1+number_2)
        elif operador == "-":
            print(number_1-number_2)
        elif operador == "/":
            print(number_1/number_2)
        elif operador == "*":
            print(number_1*number_2)
        elif operador == "sair" or operador == "Sair":
            break
        else:
            print('Não existe esse operador')
