import os
os.system('cls')

t = int(input("Digite o número a ser multiplicado durante a tabuada: "))
i = int(input("Digite o valor inicial da tabuada: "))
f = int(input("Digite o valor final da tabuada: "))

for x in range(i, f + 1):
    print(f"{t} * {x} = {t * x}")
    x += 1