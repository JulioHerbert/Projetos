linhas = 8
colunas = 5
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input(f"Digite um valor na matriz para posição: ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)
menorValor = matriz[0][0]
posicaoMenor = (0, 0)
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < menorValor:
            menorValor = matriz[i][j]
            posicaoMenor = (i, j)
print('--'*30)
print(f"Menor valor da matriz: {menorValor}")
print(f"Posição do menor valor da matriz: {posicaoMenor}")
print('--'*30)