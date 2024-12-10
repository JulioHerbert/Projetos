import time
produtos = list()
preços = list()
cont = temp = 1
while True:
    nom = str(input('qual nome do produto?: ')).strip()
    custo = float(input('digite o preço do produto: '))
    frete = float(input('digite o preço do frete: '))
    lucro = float(input('digite o lucro estimado: '))
    preço_venda = (custo + frete + lucro)
    print(f'preço da venda vai ser: R$ {preço_venda:.2f}')
    preços.append(preço_venda)
    produtos.append(nom)
    while True:
        conti = str(input('deseja continuar? [S] ou [N]: ')).upper().strip()
        if conti == 'S' or conti == 'N':
            break
        print(f'ERRO! Por favor digite somente [S] OU [N]')
    if conti == 'N':
        break
print(f'LISTA SENDO GERADA...')
time.sleep(1)
print(f'-='*30)
for c in produtos:
    print(f'{cont}º PRODUTO: {c:<15}')
    print()
    cont = cont + 1
print(f'-='*30)
for i, t in enumerate(preços):
    print(f'{temp}º PREÇO: {t}')
    print()
    temp = temp + 1
print(f'-='*30)
print(f'PROGRAMA ENCERRADO!')
            