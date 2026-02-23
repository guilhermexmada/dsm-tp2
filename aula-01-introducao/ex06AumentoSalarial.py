sal = float(input("Digite seu salário mensal em R$: "))
perc = int(input("Digite o percentual de aumento: "))

novoSal = ((sal * perc) / 100) + sal

print(f"Seu novo salário é de R$ {novoSal:.0f},00 após um aumento de {perc}%")