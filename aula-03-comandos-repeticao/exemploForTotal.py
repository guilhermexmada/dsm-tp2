# exemplo for usando range para somar os valores da sequência
import os 
os.system('cls')

total = 0
for i in range(1, 101): # por padrão a qtd de passos = 1 e sempre ignora o último número (corre de 1 até n - 1) no caso vai até 100
    total += i
print(f"A soma total de 1 a 101 é {total}")
