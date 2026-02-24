import os
os.system('cls')

# Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguinte menu.1  Média ponderada, com pesos 2 e 3, respectivamente2. Quadrado da soma dos 2 números 3. Cubo do menor número Escolha uma opção:De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

o = int(input("Escolha uma das opções: \n 1 - Média ponderada com pesos 2 e 3, respectivamente \n 2 - Quadrado da soma dos 2 números \n 3 - Cubo do menor número \n"))

if o == 1:
    print(f"Resultado = {((n1*2) + (n2*3)) / 5}")
elif o == 2:
    print(f"Resultado = {pow((n1 + n2), 2)}")
elif o == 3:
    if n1 > n2:
        print(f"Resultado = {n2**3}")
    else: 
        print(f"Resultado = {n1**3}")
else:
    print("Opção Inválida")

