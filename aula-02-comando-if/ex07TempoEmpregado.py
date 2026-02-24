import os 
os.system('cls')

# Faça um algoritmo que leia: o RG do empregado , o ano de seu nascimento e o ano de seu ingresso na empresa, e  ano atual. O programa deverá calcular e escrever a idade e o tempo  de trabalho do empregado idade =  anoatual– anonascimentotempotrabalho = anaoatual– anoingresso-Ter no mínimo 65 anos de idade. Para estar em condições de aposentadoria, um dos seguintes requisitos deve ser:'Requerer aposentadoria’-Ter o tempo trabalho no mínimo 30 anos.'Requerer aposentadoria’-Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos   'Requerer aposentadoria’ Caso não satisfaça nenhuma das condições mostre: 'Não requerer Aposentadoria'.

rg = input("Digite o RG do empregado: ")
anoNasc = int(input("Digite o ano do seu nascimento: "))
anoIng = int(input("Digite o ano de ingresso na empresa: "))
anoAt = int(input("Digite o ano atual: "))

idade = anoAt - anoNasc
tempoTrab = anoAt - anoIng

if idade >= 65:
    print("Requer aposentadoria")
elif idade >= 60 and tempoTrab >= 25:
    print("Requer aposentadoria")
elif tempoTrab >= 30:
    print("Requer aposentadoria")
else:
    print("Não requer aposentadoria")