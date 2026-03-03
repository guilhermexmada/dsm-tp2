import os
os.system('cls')

n = int(input("Digite o número para gerar a tabuada: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
    i += 1