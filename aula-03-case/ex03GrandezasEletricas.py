import os
os.system('cls')

#

g = int(input("========= CÁLCULO DE GRANDEZAS ELÉTRICAS ========= \n 1 - Tensão (em Volts) --------- U = R * i \n 2 - Resistência (em Ohm) --------- R = U / i \n 3 - Corrente (em Ampére) --------- i = U / R \n" + ("=" * 50) + "\n"))

match g:
    case 1: 
        r = int(input("Digite o valor da resistência: "))
        i = int(input("Digite o valor da corrente: "))
        u = r * i
        print(f"U = {u} V")
    case 2:
        u = int(input("Digite o valor da tensão: "))
        i = int(input("Digite o valor da corrente: "))
        r = u / i
        print(f"R = {r} Ohms")
    case 3:
        r = int(input("Digite o valor da resistência: "))
        u = int(input("Digite o valor da tensão: "))
        i = u / r
        print(f"i = {i} A")
    case _:
        print("Opção inválida")