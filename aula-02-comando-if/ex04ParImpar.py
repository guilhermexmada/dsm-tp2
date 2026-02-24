import os
os.system('cls')

# Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve mostrar o valor calculado e dizer se o número é impar ou par.Se o resto da divisão for zero, significa que o número é par if num % 2 == 0

num = int(input('Digite um número inteiro positivo: '))

if num % 2 == 0:
    print(f"{num} é PAR e {num}² = {pow(num,2)}")
else:
    print(f"{num} é ÍMPAR e {num}³ = {pow(num,3)}")