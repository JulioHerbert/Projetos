listaDeFuncionario = []
contadorDaInterface = 0
contador = 1
while True:
    if contadorDaInterface == 0:
        print(f'{"<<<PROGRAMA PARA LER SÁLARIO MENSAL>>>":^{75}}')
    print('-='*40)
    nomeDoFuncionario = str(input('Digite o nome do funcionário: '))
    sálarioMensal = float(input('Digite o sálario mensal: '))
    percentualDeReajuster = float(input('Digite o percentual de reajuster: '))
    calculo = (sálarioMensal / percentualDeReajuster) * 100
    print('-='*40)
    print('Dados do funcionário atual: ')
    print(f'Nome: {nomeDoFuncionario}')
    print(f'Percentual de aumento do sálario de {nomeDoFuncionario}: {calculo:.2f}%')
    while True:
        print('-='*40)
        adicionar = input('Você deseja adicionar esse funcionário aos dados? [S/N]: ').strip().upper()
        if adicionar == 'S':
            listaDeFuncionario.append({"Nome": nomeDoFuncionario, "Sálario": sálarioMensal, "Percentual": percentualDeReajuster,
                                       "calculo": calculo
    })
            break
        if adicionar == 'N':
            break
        else:
            print('Opção Inválida!')
    while True:
        print('-='*40)
        continuar = input('Você deseja continuar no programa? [S/N]: ').strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            contadorDaInterface = contadorDaInterface + 1
            break
        print(f'Opção Inválida!')
    if continuar == 'N':
        break
for temp in listaDeFuncionario:
    print('=='*40)
    print(f'{contador}º Nome: {temp["Nome"]}\nSálario: R$ {temp["Sálario"]:.2f}\nPercentual de reajuster: {temp["Percentual"]:.2f}%\nPercentual de aumento do sálario: {temp["calculo"]:.2f}%')
    contador = contador + 1
print('=='*40)
