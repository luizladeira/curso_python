"""
    isnumeric - checa se tem somente números e positivos
    isdigit
    isdecimal

"""
num1 = input("Digite um número: ")
num2 = input("Digite um número: ")

#isnumeric
print(num1.isnumeric())
print(num2.isnumeric())

#isdigit
print(num1.isdigit())
print(num2.isdigit())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print("Não pude converter os números para realizar sua soma...")


#TRY and EXCEPT
try:
     num1 = float(num1)
     num2 = float(num2)
     print(num1+num2)
except:
    print('ERRORRR......')
