import os 
os.system('cls')

# faça um programa que verifique se uma letra digitada é consoante ou vogal

l = input("Digite uma letra: ")

match l.upper():
    case "A":
        print(f"{l} é vogal")
    case "E":
        print(f"{l} é vogal")
    case "I":
        print(f"{l} é vogal")
    case "O":
        print(f"{l} é vogal")
    case "U":
        print(f"{l} é vogal")
    case _:
        print(f"{l} é consoante")