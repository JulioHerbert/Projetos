SomaPares = 0
ContadorPares = 0
matriz = []
for i in  range(5):
    linha = []
    for j in range(6):
        valor = int(input(f"digite um valor na posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            SomaPares = SomaPares + valor
            ContadorPares = ContadorPares + 1
if ContadorPares > 0:
    mediaPares = SomaPares / ContadorPares
else:
    mediaPares = 0
print("Contéudo da matriz:")
for linha in matriz:
    print(linha)
print(f"\nMédia dos valores pares da matriz: {mediaPares:.2f}")