HistoricoCalculadora = []
cont = 1
print(f'Basta digitar as base respectivas do TRAPÉZIO abaixo e depois clicar "ENTER". ')
print(f'-='*40)
while True:
    LadoB = float(input('\033[mDigite o primeiro lado paralelo do TRAPÉZIO.\n\033[1;97m[BASE MAIOR]: '))
    Ladob = float(input('\033[mDigite o segundo lado paralelo do TRAPÉZIO.\n\033[1;97m[BASE MENOR]: '))
    AlturaTrapezio = float(input('\033[mDigite a altura do TRAPÉZIO.\n\033[1;97m[ALTURA]: '))
    Resultado = (LadoB + Ladob) * AlturaTrapezio / 2
    HistoricoCalculadora.append({"BaseMaior": LadoB, "BaseMenor": Ladob, "AlturaDoTrapézio": AlturaTrapezio,
                                 "Resultado": Resultado
 })
    if len(HistoricoCalculadora) == 4:
        del HistoricoCalculadora[0]

    while True:
        continuar = input('\033[1;97mContinuar com programa? [S/N]: ').upper().strip()
        if continuar == "S" or continuar == "N":
            break
        print(f'\033[31mOpção Inválida.')
    if continuar == "N":
        break
for temp in HistoricoCalculadora:
    print(f'-='*40)
    print(f'{cont + 1}º Trapézio')
    print(f'-='*40)
    print(f'BASE MAIOR = {temp["BaseMaior"]:.2f}      BASE MENOR = {temp["BaseMenor"]:.2f}')
    print(f'Altura = {temp["AlturaDoTrapézio"]:.2f}')
    print(f'Área = {temp["Resultado"]:.2f}')
    cont = cont + 1
print(f'-='*40)
print(f'Total de Cálculos relizados: {len(HistoricoCalculadora) + 1}')
print(f'Historico só mostra os 3 últimos cálculos!')