while True:
    nome = input('Qual nome do funcionário?: ')
    tempoDeServiço = int(input('Qual tempo de serviço?: '))
    SálarioDoFuncionario = float(input('Qual o sálario do funcionário?: R$ '))
    print('-'*40)
    print(f'Nome do Funcionário: {nome}')
    print(f'Tempo de Serviço: {tempoDeServiço} anos')
    print(f'Sálario do Funcionário: R$ {SálarioDoFuncionario:.2f}')
    print('-'*40)
    if tempoDeServiço >= 10 and SálarioDoFuncionario > 3000:
        print(f'Funcionário: {nome} receberá um aumento de 10%')
        aumento = SálarioDoFuncionario * (10 / 100)
        novoValor = SálarioDoFuncionario + aumento
        print(f'Aumento recebido com base no sálario: R$ { novoValor:.2f}')
    elif tempoDeServiço == 9 and SálarioDoFuncionario > 3000:
        print(f'Funcionário: {nome} receberá um aumento de 9%')
        aumentoDois = SálarioDoFuncionario * (9 / 100)
        novoValorDois = SálarioDoFuncionario + aumentoDois
        print(f'Aumento recebido com base no sálario: R$ {novoValorDois:.2f}')
    else:
        print(f'Demais funcionários: {nome} receberá um aumento de 5%')
        aumentoTres = SálarioDoFuncionario * (5 / 100)
        novoValorTres = SálarioDoFuncionario + aumentoTres
        print(f'Aumento recebido com base no sálario: R$ {novoValorTres:.2f}')
    print('-'*40)
    while True:
        continuarNoPrograma = input('Deseja continuar no programa? [S/N]: ').strip().upper()[0]
        if continuarNoPrograma == 'S' or continuarNoPrograma == 'N':
            break
        print('Opção inválida!')
    if continuarNoPrograma == 'N':
        break
print('Programa encerrado!')