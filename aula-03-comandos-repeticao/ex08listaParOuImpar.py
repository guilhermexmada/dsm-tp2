import os
os.system('cls')

lista = []

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número da lista: "))
    lista.append(num)
    i += 1
for item in lista:
    if item % 2 == 0:
        print(f"{item} | PAR")
    else:
        print(f"{item} | ÍMPAR")