"""
Trocar valores entre variaveis
"""
x = 10
y = 'Luiz'

# ONDE x é igual a y E y é igual a x
x, y = y, x
print(f'x={x} e y={y}')

z = 'Ladeira'
x, y, z = z, x, y
print(f'x={x}, y={y} e z={z}')

