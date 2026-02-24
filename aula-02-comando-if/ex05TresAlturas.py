import os
os.system('cls')

# Leia a altura de 3 pessoas. Ao fim, o programa deve mostrar as estaturas em ordem decrescente. Mostrar a pessoa de maior altura , altura mediana , e menor altura

a1 = float(input("Digite a altura da pessoa 01:"))
a2 = float(input("Digite a altura da pessoa 02:"))
a3 = float(input("Digite a altura da pessoa 03:"))

if a1 > a2 and a1 > a3:
    maior = 'pessoa 01'
    if a2 > a3:
        meio = 'pessoa 02'
        menor = 'pessoa 03'
    else:
        meio = 'pessoa 03'
        menor = 'pessoa 02'
elif a2 > a1 and a2 > a3:
    maior = 'pessoa 02'
    if a1 > a3:
        meio = 'pessoa 01'
        menor = 'pessoa 03'
    else:
        meio = 'pessoa 03'
        menor = 'pessoa 01'
elif a3 > a1 and a3 > a2:
    maior = 'pessoa 03'
    if a1 > a2:
        meio = 'pessoa 01'
        menor = 'pessoa 02'
    else:
        meio = 'pessoa 02'
        menor = 'pessoa 01'

print(f"Maior: {maior} | Meio: {meio} | Menor: {menor}")