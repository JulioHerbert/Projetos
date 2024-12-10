Continuar = ''
ContadorDaInterface = 0
while True:
    while True:
        if ContadorDaInterface == 0:
            print()
            print('C<<<CONVERSÃO DE TEMPERATURA>>>\n')
        while True:
            try:
                ValorDeGraus = float(input('Digite um valor de graus°: '))
                print()
                break
            except ValueError:
                print(f'ERRO! Por favor digite um valor númerico.')
        print('Qual tipo de temperatura esse valor possui?')
        print()
        print('[1] Farenheit\n[2] Celsius\n[3] Kelvin\n')
        while True:
            InterfaceDeInteracao = input('Digite uma das opções acima: ').upper().strip()
            print(f'\nVocê deseja converter {ValorDeGraus}° para que tipo de temperatura?')
            if InterfaceDeInteracao == "1" or InterfaceDeInteracao == "2" or InterfaceDeInteracao == "3":
                break
            print('Opção Inválida!')
        break
    print('\n[1] Farenheit\n[2] Celsius\n[3] Kelvin\n')
    while True:
        SegundaInterfaceDeInteracao = input('Digite uma das opções acima: ').upper().strip()
        if SegundaInterfaceDeInteracao == "1" or SegundaInterfaceDeInteracao == "2" or SegundaInterfaceDeInteracao == "3":
            break
        print('Opção Inválida!')
    #Cálculo de Farenheit para Celsius:
    if InterfaceDeInteracao == "1" and SegundaInterfaceDeInteracao == "2":
        CalculoFarenheitParaCelsius = (ValorDeGraus - 32) / 1.8
        print(f'\nResultado da Conversão de Farenheit para Celsius: {CalculoFarenheitParaCelsius:.2f}°C\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
    #Cálculo de Farenheit para Kelvin:
    if InterfaceDeInteracao == "1" and SegundaInterfaceDeInteracao == "3":
        CalculoFarenheitParaKelvin = (ValorDeGraus - 32) * 5/9 + 273.15
        print(f'\nResultado da Conversão de Farenheit para Kelvin: {CalculoFarenheitParaKelvin:.2f}°K\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
    #Cálculo Celsius para Farenheit:
    if InterfaceDeInteracao == "2" and SegundaInterfaceDeInteracao == "1":
        CalculoCelsiusParaFarenheit = (ValorDeGraus * 9/5) + 32
        print(f'\nResultado da Conversão de Celsius para Farenheit: {CalculoCelsiusParaFarenheit:.2f}°F\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
    #Cálculo Celsius para Kelvin:
    if InterfaceDeInteracao == "2" and SegundaInterfaceDeInteracao == "3":
        CalculoCelsiusParaKelvin = (ValorDeGraus + 273.15)
        print(f'\nResultado da Conversão de Celsius para Kelvin: {CalculoCelsiusParaKelvin:.2f}°K\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opcão Inválida!')
        if Continuar == 'N':
            break
    #Cálculo Kelvin para Celsius:
    if InterfaceDeInteracao == "3" and SegundaInterfaceDeInteracao == "2":
        CalculoKelvinParaCelsius = (ValorDeGraus - 273.15)
        print(f'\nResultado da Conversão de Kelvin para Celsius: {CalculoKelvinParaCelsius:.2f}°C\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
    #Cálculo Kelvin para Farenheit:
    if InterfaceDeInteracao == "3" and SegundaInterfaceDeInteracao == "1":
        CalculoKelvinParaFarenheit = (ValorDeGraus - 273.15) * 9/5 + 32
        print(f'\nResultado da Conversão de Kelvin para Farenheit: {CalculoKelvinParaFarenheit:.2f}°F\n')
        while True:
            Continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
    if InterfaceDeInteracao == SegundaInterfaceDeInteracao:
        print(f'\nValor não alterado: {ValorDeGraus:.2f}\n')
        while True:
            Continuar = input('Você deseja continuar no programa [S/N]: ').upper().strip()[0]
            if Continuar == 'S' or Continuar == 'N':
                ContadorDaInterface =+ 1
                break
            print('Opção Inválida!')
        if Continuar == 'N':
            break
print(f'PROGRAMA ENCERRRADO.')