import os
os.system('cls')

# Construa um programa que receba o nome e peso de duas pessoas e mostre o nome e o peso da pessoa mais pesada ,e verifica se as pessoas tem o mesmo peso

n1 = input("Digite o nome da primeira pessoa: ")
p1 = float(input("Digite o peso em kg da primeira pessoa: "))
n2 = input("Digite o nome da segunda pessoa: ")
p2 = float(input("Digite o peso em kg da segunda pessoa: "))

if p1 == p2:
    print(f"{n1} e {n2} pesam o mesmo: {p1} kg")
elif p1 > p2:
    print(f"{n1} é mais pesado(a) que {n2}")
else:
    print(f"{n2} é mais pesado(a) que {n1}")
