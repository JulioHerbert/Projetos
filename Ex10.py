ContadorDaInterface = 0
continuar = ''
while True:
    while True:
        if ContadorDaInterface == 0:
            print(f'{"<<<CONVERSO DE TEMPERATURA>>>":^{45}}\n')
            print(f'\n\033[1;97m[1] Farenheit para Celsius\033[m')
            print(f'\033[1;97m[2] Celsius para Farenheit\033[m\n')
        while True and ContadorDaInterface == 1:
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).upper().strip()
            if continuar == 'S' or continuar == 'N':
                break
            print(f'Opção Inválida!')
        if continuar == 'N':
            break
        ValorDeGraus = float(input('Digite valor do grau° para conversão: '))
        InterfaceDeInteracao = (input('Digite uma das opções acima: ')).upper()
        if InterfaceDeInteracao == "1" or InterfaceDeInteracao == "2":
            break
        print(f'\033[31mOpção Inválida!\033[m')
        ContadorDaInterface =+ 1
            
    if InterfaceDeInteracao == "1":
        ContadorDaInterface =+ 1
        CalculoFarenheit = (ValorDeGraus - 32) / 1.8
        print(f'\nResultado da Conversão de Farenheit para Celsius: °F {CalculoFarenheit:.2f}\n')
        break
    elif InterfaceDeInteracao == "2":
        ContadorDaInterface =+ 1
        CalculoCelsius = (ValorDeGraus * 9/5 ) + 32
        print(f'\nResultado da Conversão de Celsius para Farenheit: °C {CalculoCelsius:.2f}\n')
        break
print(f'PROGRAMA ENCERRRADO.')
