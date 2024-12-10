n1 = []
for temp in range(5):
    n1.append(int(input(f'Digite o valor da {temp+1}º posição: ')))
print('\nOrdem Invertida:')
for temp in range(4, -1, -1):
    print(f'{temp}º valor: {n1[temp]}')