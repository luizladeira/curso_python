"""

Criar variáveis para nome (str), idade (int)
Altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings

"""
import datetime

nome = 'Luiz Ladeira'
altura = 1.63
peso = 62.200
ano_nascimento = 1990
data_agora = datetime.date.today()
ano_atual = data_agora.strftime("%Y")
idade_cont = (int(ano_atual))-ano_nascimento
imc = peso/(altura*altura)

print("{nom} possui altura {alt} cm e peso {peso}. Seu ano de nascimento é {nac} e estamos no ano {atual}, portanto ele possui {idade_cont}. Seu IMC é {im:.2f} kg/m2".format(nom=nome, alt=altura, peso=peso, nac=ano_nascimento, atual=ano_atual, idade_cont= idade_cont ,im=imc))

