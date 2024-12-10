n1 = list()
n2 = list()
cont = temp = 1
while True:
    num = int(input('quantos números INTEIROS você deseja somar?: '))
    for c in range(0, num):
        num1 = int(input(f'digite o {cont}º valor: [INTEIRO] '))
        n1.append(num1)
        cont = cont + 1
    num2 = int(input('quantos números REAIS você deseja somar?: '))
    for c in range(0, num2):
        num2 = float(input(f'digite o {temp}º valor: [REAL] '))
        n2.append(num2)
        temp = temp + 1
    print(f'A soma dos números REAIS resultou em: {sum(n2)}')
    print(f'A soma dos números INTEIROS e REAIS resultou em: {sum(n1+n2):.2f}')
    while True:
        conti = str(input('você deseja continuar? [S] ou [N]: ')).upper().strip()
        if conti == 'S' or conti == 'N':
            break
        print(f'ERRO! Por favor digite somente [S] OU [N]. ')
    if conti == 'N':
        break
print(f'A soma dos números INTEIROS resultou em: {sum(n1)}')
print('USUÁRIO ENCERROU O PROGRAMA...')


