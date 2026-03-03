# exemplo de for usando uma lista de valores pré-definida
import os
os.system('cls')

# percorrendo array
frutas = ['banana','maçã','laranja','uva','melancia','abacaxi']
for item in frutas:
    print(item)

# procurando item no array
buscar = 'laranja'
frutas = ['banana','maçã','laranja','uva','melancia','abacaxi']
for item in frutas:
    if item == 'laranja':
        print(f"fruta encontrada: {buscar}")
        break # encerra a execução do loop
    else:
        print(f"{buscar} não encontrado")
