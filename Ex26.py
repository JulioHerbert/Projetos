while True:
    TabelaJuros = {"Até 30 dias": 0.05,
                "De 30 a 60 dias": 0.10,
                "Acima de 60 dias": 0.15
    }
    valorParcela = float(input('Digite o valor da parcela: '))
    Dias = int(input('Digite quantos dias de atraso: '))

    if Dias <= 30:
        taxaDeJuros = TabelaJuros["Até 30 dias"]
    elif Dias <= 60:
        taxaDeJuros = TabelaJuros["De 30 a 60 dias"]
    else:
        taxaDeJuros = TabelaJuros["Acima de 60 dias"]
    juros = valorParcela * taxaDeJuros
    valorTotal = valorParcela + juros
    print(f'Valor do juros: R$ {juros:.2f}')
    print(f'Valor total a ser pago: R$ {valorTotal:.2f}')
    while True:
        continuar = str(input('Você deseja reiniciar o programa? [S/N]: ')).upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção Inválida!')
    if continuar == 'N':
        break
print('Programa encerrado!')