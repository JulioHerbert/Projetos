Vetor = []
cont = ordem = 1
for user in range(0, 5):
    Vetor.append(int(input(f'Digite {cont}º valor de número inteiro: ')))
    cont = cont + 1
vetorOrdenado = sorted(Vetor, reverse=True)
print('=='*40)
print(f'ORDENANDO OS VALORES DO MAIOR PARA O MENOR:\n')
for temp in vetorOrdenado:
    print(f'{ordem}º valor {temp}')
    ordem = ordem + 1
print('=='*40)