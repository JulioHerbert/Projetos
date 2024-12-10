n1 = []
contador = contador2 = 1
for temp in range(1, 6):
    n1.append(int(input(f'digite primeira posição {temp}º número: ')))
OrdemCrescente = sorted(n1, reverse=False)
OrdemDecrescente = sorted(n1, reverse=True)
print('\nOrdem crescente:')
for temp in OrdemCrescente:
    print(f'{contador}º valor: {temp}')
    contador += 1
print()
print('\nOrdem decrescente:')
for temp in OrdemDecrescente:
    print(f'{contador2}º valor: {temp}')
    contador2 += 1
print()
