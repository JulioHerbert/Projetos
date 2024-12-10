from datetime import datetime
HistoricosCorridas = []
Contador = 0
ContadorDaInterface = 0
while True:
    if ContadorDaInterface == 0:
        print(f'{"<<<LEITOR DE MINUTOS>>>":^{75}}')
    print('-=' * 40)
    horaInicial = int(input('Digite hora inicial da caminhada: '))
    minutosInicial = int(input('Digite minuto inicial da caminhada: '))
    print('-=' * 40)
    horaFinal = int(input('Digite hora final da caminhada: '))
    minutosFinal = int(input('Digite minutos final da caminhada: '))
    print('-=' * 40)
    distânciaTotalPercorrida = float(input('Digite a distância total percorrida em metros: '))
    print('==' * 40)
    TotalMinutosInicial = horaInicial * 60 + minutosInicial
    TotalMinutosFinal = horaFinal * 60 + minutosFinal
    TotalMinutosPercorridos = TotalMinutosFinal - TotalMinutosInicial

    distanciaPercorridaPorMinuto = distânciaTotalPercorrida / TotalMinutosPercorridos
    DataAtual = datetime.now()
    FormatacaoData = DataAtual.strftime('%d/%m/%Y')
    FormatacaoHora = DataAtual.strftime('%H:%M')
    print(f'A quantidade de minutos percorridos foi de: {TotalMinutosPercorridos} minutos.')
    print(f'A distância percorrida por minutos foi de: {distanciaPercorridaPorMinuto:.2f} metros/minuto.')
    print('==' * 40)
    while True:
        SaveCorridas = input('Deseja salvar essa corridas? [S/N] ').upper().strip()[0]
        if SaveCorridas == 'S':
            HistoricosCorridas.append({"DATA": FormatacaoData, "HORA": FormatacaoHora, "TotalMinutosIniciais": TotalMinutosInicial, "TotalMinutosFinais": TotalMinutosFinal,
                                  "TotalMinutosPercorridos": TotalMinutosPercorridos, "DistanciaPercorridos": distanciaPercorridaPorMinuto
    })
            print('Corrida salva com sucesso!')
            break
        if SaveCorridas == 'N':
            break
        else:
            print('Opção Inválida!')  
    while True:
        continuar = input('Deseja continuar no programa? [S/N] ').upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            ContadorDaInterface =+ 1
            break
        print('Por favor digite somente [S] ou [N].')
    if continuar == 'N':
        break
if Contador == 0:
    print('-' * 40)
    print('CORRIDAS SALVAS:')
    print('-' * 40)
    Contador = Contador + 1
for temp in HistoricosCorridas:
    print(f'DATA: {temp["DATA"]}')
    print(f'[{temp["HORA"]}] A quantidade de minutos percorridos foi de: {temp["TotalMinutosPercorridos"]} minutos.')
    print(f'[{temp["HORA"]}] A distância percorrida por minutos foi de: {temp["DistanciaPercorridos"]:.2f} metros/minutos.')
    print('-' * 40)

