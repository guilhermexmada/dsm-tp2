num = float(input("Digite um número: "))
exp = int(input("Digite um expoente: "))

# potencia utilizando operador aritmético
potencia = num ** exp

# potencia utilizando função nativa math
pot = pow(num, exp)

print(f"{num} ^ {exp} = {potencia} = {pot:.0f}") 