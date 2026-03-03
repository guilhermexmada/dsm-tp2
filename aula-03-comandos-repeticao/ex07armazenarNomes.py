import os
os.system('cls')

i = 0
e = 0
nomes = []

while i <= 6:
    n = input(f"Digite o {i + 1}º nome da lista: ")
    nomes.append(n)
    i += 1

print("\n Nomes digitados: \n")

while e <= 6:
    print(f"{nomes[e]}")
    e += 1
