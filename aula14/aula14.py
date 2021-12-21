"""
Formatando valores com modificadores

:s - TEXTO (strings)
:d - Inteiros (int)
:f - Número de ponto de flutuante (float)
:.(Númeor)f - Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ) (Quantidade)(Tipo -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

numero_1 = 10
numero_2 = 3
divisao = numero_1 / numero_2
print('{:.2f}'.format(divisao))  #divisao com 2 numero
print(f'{divisao:.2f}')  #divisao com 2 numero

#STRINGS :s

nome = 'Luiz Ladeira'
print(f'{nome:s}')  #falando que ela é uma string mais nada

#TAMANHO DE STRING TENHA UM VALOR PADRÃO

print(f'{numero_1:0>10}')  #falo que minha variavel deve ter 10 casas a direita
print(f'{numero_1:0<10}')  #falo que minha variavel deve ter 10 casas a esquerda
print(f'{numero_1:0^10}')  #falo que minha variavel deve ter 10 casas e ficará ao centro
print(f'{numero_1:.2f}')   #falo que minha variavel deve ter 2 casas decimais
print(f'{numero_1:0>10.2f}')  #falo que minha variavel deve ter 10 casas a direita com duas casas decimais


#TAMANHO DE STRING TENHA UM VALOR PADRÃO

print(f'{nome:#^50}')
print(50-len(nome)/2)
nome_formatado = "{n:@>30}".format(n=nome)
print(nome_formatado)

#CHAMANDO POR INDICES

nome_indice = "Luiz Paulo"
sobrenome_indice = "Araujo Ladeira"
nome_formatado_indice = '{0:*^50}{1:|^50}'.format(nome, sobrenome_indice)
print(nome_formatado_indice)

# TRATATIVAS DE STRINGS
nome_tres = 'lUiZ PaUlO'
print(nome_tres.ljust(20, '&'))   #justifica a esquerda e preenche até dar 20 caracteres
print(nome_tres.upper())   #Todas as letras maiusculas
print(nome_tres.title())   #Primeiras letras maiusculas
