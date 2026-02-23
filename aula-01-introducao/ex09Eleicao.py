brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

eleitores = brancos + nulos + validos

percBranco = (brancos * 100) / eleitores
percNulos = (nulos * 100) / eleitores
percValidos = (validos * 100) / eleitores

print(f"Porcentagem de votos brancos: {percBranco:.1f}% \n Porcentagem de votos nulos: {percNulos:.1f}% \n Porcentagem de votos válidos: {percValidos:.1f}%")

