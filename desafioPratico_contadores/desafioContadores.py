"""
Criar uma estrutura de repitação com dois contadores um de maneira progressiva: 0,1,2,3,4,5,6,7,8,9,10
e outra de maneira regressiva: 10,9,8,7,6,5,4,3,2
"""

contador_progressivo = 0
contador_regressivo = 10

while contador_progressivo <= 10 and contador_regressivo <= 10:
    print(contador_progressivo, '<->', contador_regressivo)
    contador_progressivo += 1
    contador_regressivo -= 1