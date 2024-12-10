from datetime import datetime
ValoresSalvos = []
ContadorDaInterface = 0
while True:
    if ContadorDaInterface == 0:
        print(f'{"<<<EXERCÍCIO 25>>>":^{75}}')
    ValorInicialOdometro = float(input('Digite o valor inicial do odômetro [Km]: '))
    ValorFinalOdometro = float(input('Digite o valor final do odômetro [Km]: '))
    QuantidadeDeLitrosAbastecidos = float(input('Digite a quantidade de litros abastecidos no final da viagem [Litros]: '))
    QuantidadeDeQuilometrosPercorridos = ValorFinalOdometro - ValorInicialOdometro
    ConsumoDeCombustivelPorQuilometros = QuantidadeDeLitrosAbastecidos / QuantidadeDeQuilometrosPercorridos
    DataAtual = datetime.now()
    FormatacaoData = DataAtual.strftime('%d/%m/%Y')
    FormatacaoHora = DataAtual.strftime('%H:%M')
    print('==' * 40)
    print('Agora.')
    print(f'Quantidade de quilometros percorridos: {QuantidadeDeQuilometrosPercorridos:.2f} km')
    print(f'Quantidade de litros consumidos por quilometro: {ConsumoDeCombustivelPorQuilometros:.2f} metros/km')
    print('==' * 40)
    while True:
        SalvarValores = input('você deseja salvar os valores digitados acima? [S/N]: ').upper().strip()[0]
        if SalvarValores == 'S':
            ValoresSalvos.append({"Data": FormatacaoData, "Hora": FormatacaoHora, "Quilometros percorridos": QuantidadeDeQuilometrosPercorridos, "Litros consumidos por quilometros": ConsumoDeCombustivelPorQuilometros
    })
            print('Valores salvos com sucesso!')
            break
        if SalvarValores == 'N':
            break
        else:
            print('Opção Inválida!')
    while True:
        continuar = input('você deseja continuar no programa? [S/N]: ').upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            ContadorDaInterface =+ 1
            break
        print('Opção Inválida!_2')
    if continuar == 'N':
        break
print('\nHistorico dos Valores salvos:')
for temp in ValoresSalvos:
    print('--' * 40)
    print(f'Data: {temp["Data"]}')
    print(f'[{temp["Hora"]}] Quantidade de quilometros percorridos: {temp["Quilometros percorridos"]:.2f} km')
    print(f'[{temp["Hora"]}] Quantidade de litros consumidos por quilometro: {temp["Litros consumidos por quilometros"]:.2f} metros/km')
print('--' * 40)
print('Program encerrado...')
                                                                

