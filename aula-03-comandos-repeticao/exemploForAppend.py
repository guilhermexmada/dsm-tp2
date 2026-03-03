import os 
os.system('cls')

# exemplo de for usando Append para adicionar valores à lista

numeros = []

# incrementando 
for i in range(1,11):
    n = int(input(f"Digite o {i}º número: "))
    numeros.append(n)

# exibindo
for item in numeros:
    print(item)