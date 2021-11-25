"""
Operadores Lógicos

+, -, *, /, // -> divisão inteira, ** -> exponenciação, % -> retorna o resto da divisão, () -> alterar as precedencias

"""

#SOMA
print('SOMA: ', 10 + 10)

#SUBTRAÇÃO
print('SUBTRAÇÃO: ', 10 - 5)

#MULTIPLICAÇÃO
print('MULTIPLICAÇÃO: ', 10 * 2)

#DIVISÃO
print('DIVISÃO: ', 10 / 2)

#DIVISÃO INTEIRA
print('DIVISÃO INTEIRA: ', 123.33 // 10)

#EXPONENCIAÇÃO
print('EXPONENCIAÇÃO: ', 2 ** 8)

#RESTO DA DIVISÃO
print('RESTO DA DIVISÃO: ', 100 % 5)

#ALTERAR PRECEDENCIAS
print('PRECEDENCIAS: ', ((10*2)+(5+2))*10 )

"""
( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

https://docs.python.org/3/reference/expressions.html#operator-precedence

"""

print('Exemplo: (2 + 5 * 3) ** 2 - (23.5 + 23.5) = ', (2 + 5 * 3) ** 2 - (23.5 + 23.5))