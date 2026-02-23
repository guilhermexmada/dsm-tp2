nome = input("Digite o nome do produto")
quant = int(input("Digite a quantidade comprada: "))
precoUnit = float(input("Digite o preço unitário: "))

total = quant * precoUnit

print(f"Total a pagar de R$ {total:.2f} por {quant} unidades de {nome} a R$ {precoUnit:.2f}")