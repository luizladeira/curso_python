"""
  * Laço de Repetição - While / Else
  * Contadores
  * Acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(f'---\nContador: {contador}')
    acumulador = acumulador+contador
    print(f'Acumulador: {acumulador}\n')
    contador += 1
else:
    print(f'Ele executa o bloco ELSE do While')

