import os
os.system('cls')

# 

i = int(input("Digite o índice de poluição causado pela sua empresa: "))

match i:
    case 0 | 1 | 2:
        print("Considerado aceitável")
    case 3 | 4 | 5:
        print("Grupo 1: Suspender atividades")
    case 6 | 7:
        print("Grupo 2: Suspender atividades")
    case 8:
        print("Suspender atividade de todos os grupos")
    case _:
        if i > 8:
            print("Suspender atividades de todos os grupos")
        else:
            print("Índice inválido")