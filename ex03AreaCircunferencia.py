import math

raio = float(input("Digite o valor do raio do poço em centímetros: "))

area = pow(raio, 2) * 3.14

print(f"A área da circunferência é de aprox. {area} cm²")

a = math.pi*(raio ** 2) # usando a importação da função math 