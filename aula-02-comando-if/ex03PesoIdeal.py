import os
os.system('cls')

# Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo. Elabore um algoritmo que leia a altura e o sexo(M/F) de uma pessoa, calcule e mostre o  seu peso ideal, utilizando as seguintes fórmulas. Para Masculino :  (72.7*altura)–58 Para Feminino :  (62.1*altura)–44.7 No final mostre a altura ,o sexo e peso ideal

a = float(input('Digite a altura da pessoa 01 em metros: '))
s = input('Digite o sexo da pessoa 01 (F-feminino M-masculino): ')

if s.upper() == "M":
    p = (72.7 * a) - 58
    s = "masculino"
elif s.upper() == "F":
    p = (62.1 * a) - 44.7
    s = "feminino"

print(f'Para uma pessoa com {a} m de altura do sexo {s} o peso ideal é de {p} kg')
