ContadorDaInterface = 0
ContadorDoPrograma = []
continuar = ''
#SISTEMA DE LOOP:
while True:
    while True:
        #ELABORAÇÃO DA INTERFACE:
        if ContadorDaInterface == 0:
            print(f'{"<<<CONVERSO DE TEMPERATURA>>>":^{45}}')
            print()
        while True:
            try:
                ValorDeGraus = float(input('Digite um valor númerico para conversão: '))
                break
            except ValueError:
                print(f'\033[31mERRO! Por favor digite um valor númerico.\033[m')
        print(f'\n\033[1;97m[1] Farenheit para Celsius')
        print(f'[2] Celsius para Farenheit')
        print(f'[3] Kelvin para Celsius')
        print(f'[4] Kelvin para Farenheit')
        print(f'[5] Celsius para Kelvin')
        print(f'[6] Farenheit para Kelvin\033[m\n')
        #ELABORAÇÃO DA INTERAÇÃO DA INTERFACE COM USUÁRIO:
        while True:
            InterfaceDeInteracao = (input('Digite uma das opções acima: ')).strip().upper()
            if InterfaceDeInteracao == "1" or InterfaceDeInteracao == "2" or InterfaceDeInteracao == "3" or InterfaceDeInteracao == "4" or InterfaceDeInteracao == "5" or InterfaceDeInteracao == "6":
                break
            print(f'\033[31mOpção Inválida!\033[m')
        break
        #ELABORAÇÃO DOS CÁLCULOS UTILIZANDO AS FÓRMULAS:
    if InterfaceDeInteracao == "1":
        CalculoFarenheitParaCelsius = (ValorDeGraus - 32) / 1.8
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoFarenheitParaCelsius:.2f}°C\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoFarenheitParaCelsius:.2f}°C\033[m\n')
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[31mOpção Inválida!\033[m')
        if continuar == 'N':
            break
    elif InterfaceDeInteracao == "5":
        CalculoCelsiusParaKelvin = (ValorDeGraus + 273.15)
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoCelsiusParaKelvin:.2f}°K\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoCelsiusParaKelvin:.2f}°K\033[m\n')
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[1;97mOpção Inválida!\033[m')
        if continuar == 'N':
            break
    elif InterfaceDeInteracao == "3":
        CalculoKelvinParaCelsius = (ValorDeGraus - 273.15)
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoKelvinParaCelsius:.2f}°C\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoKelvinParaCelsius:.2f}°C\033[m\n')
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[31mOpção Inválida!\033[m')
        if continuar == 'N':
            break
    elif InterfaceDeInteracao == "4":
        CalculoKelvinParaFarenheit = (ValorDeGraus - 273.15) * 9/5 + 32
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoKelvinParaFarenheit:.2f}°F\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoKelvinParaFarenheit:.2f}°F\033[m\n')
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[31mOpção Inválida!\033[m')
        if continuar == 'N':
            break
    elif InterfaceDeInteracao == "2":
        CalculoCelsiusParaFarenheit = (ValorDeGraus * 9/5) + 32
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoCelsiusParaFarenheit:.2f}°F\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoCelsiusParaFarenheit:.2f}°F\033[m\n')
            continuar = str(input('Você deseja continuar no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[31mOpção Inválida!\033[m')
        if continuar == 'N':
            break
    elif InterfaceDeInteracao == "6":
        CalculoFarenheitParaKelvin = (ValorDeGraus - 32) * 5/9 + 273.15
        if ContadorDaInterface == 0:
            print(f'\n\033[1;97mResultado da Conversão: {CalculoFarenheitParaKelvin:.2f}°K\033[m\n')
        while True:
            if continuar == 'S':
                print(f'\n\033[1;97mResultado da Conversão: {CalculoFarenheitParaKelvin:.2f}°K\033[m\n')
            continuar = str(input('Você deseja continuar? no programa? [S/N]: ')).strip().upper()[0]
            if continuar == 'N' or continuar == 'S':
                ContadorDaInterface =+ 1
                ContadorDoPrograma.append(ContadorDaInterface)
                break
            print(f'\033[31mOpção Inválida!\033[m')
        if continuar == 'N':
            break
print(f'\n\033[31mENCERRANDO...')
print(f'PROGRAMA ENCERRADO.')
(print(f'\033[mTotal de contas realizadas: {len(ContadorDoPrograma)}'))