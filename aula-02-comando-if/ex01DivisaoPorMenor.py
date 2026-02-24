import os
os.system('cls')

# Leia dois números e calcule a divisão do maior número pelo menor número . Verifique se os números são iguais, mostre mensagem avisando que os números são iguais.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    div = num1 / num2
    print(f"{num1} dividido por {num2} = {div}")
elif num2 > num1:
    div = num2 / num1
    print(f"{num2} dividido por {num1} = {div}")
else:
    print("Os dois números são iguais")