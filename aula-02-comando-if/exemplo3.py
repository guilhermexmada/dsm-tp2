import os
os.system('cls')

print('$$$ Programa de Empréstimo $$$ \n Responda(0-Não 1-Sim)')

neg = int(input('Possui nome negativo? '))

if neg == 1:
    print('Você não pode realizar empréstimo')
else:
    cartass = int(input('Você possui carteira assinada? '))
    if cartass == 0:
        print("Você não pode realizar empréstrimo")
    else:
        casa = int(input("Você possui casa própria? "))
        if casa == 0:
            print("Você não pode realizar empréstimo")
        else:
            print("Conceder o empréstimo")