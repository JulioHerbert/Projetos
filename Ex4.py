regit = list()
dado = list()
cont = 1
while True:
    dado.append(str(input('nome: ')).strip())
    dado.append(str(input('qual nome do livro?: ')).strip())
    multa = float(input('qual valor da multa?: R$ '))
    dias = int(input('digite quantos dias de atraso: '))
    dado.append(multa)
    dado.append(dias)
    valormulta = (dias*multa)
    regit.append(dado[:])
    dado.clear()
    while True:
        conti = str(input('você deseja continuar? [S] ou [N]: ')).upper().strip()
        if conti == 'S' or conti == 'N':
            break
        print(f'ERRO! Por favor digite somente [S] OU [N]. ')
    if conti == 'N':
        break
print(f'-='*30)
for temp in regit:
    print(f'{cont}º Nome: {temp[0]}\n{"Livro: ":>10}{temp[1]}\n{"Multa: ":>10}{temp[2]}')
    cont = cont + 1
    print(f'-='*30)
print(f'PROGRAMA ENCERRADO...')
print(f'Total de pessoas cadastradas: {cont-1}')