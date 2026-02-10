varDeslocamento = float(input("Digite a variação do deslocamento do veículo em mts: "))
varTempo = float(input("Digite a variação do tempo em min: "))

velocMedia = varDeslocamento / (varTempo * 60)

print(f"Sua velocidade média é de {velocMedia} m/s")