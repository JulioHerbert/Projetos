import time
ContadorDaInterface = 0
InicioDoContadorDeTempo = time.time()
X = Y = Z = 0
while True:
    if ContadorDaInterface == 0:
        print(f'-=' * 30)
        print('ATIVIDADE COM ELABORAÇÃO DE EXPRESSÕES SENDO ELAS: X, Y e Z.')
        print(f'-=' * 30)
        print()
    while True:
        try:
            X = float(input('Digite o valor da expressão X: '))
            Y = float(input('Digite o valor da expressão Y: '))
            Z = float(input('Digite o valor da expressão Z: '))
            print()
            break
        except ValueError:
            print(f'ERRO! Por favor digite um valor númerico.')

    #ELABORAÇÃO DOS CÁLCULOS UTILIZANDO AS EXPRESSÕES:
    A = (X < Y) and (Y < Z)
    B = (X > Y) and (Y < Z)
    C = (X < Y) or (Y < Z)
    D = (X < Y) or (Y > Z)
    E = (X > Y) or (Y < Z)

    #RESULTADO DOS CÁLCULOS UTILIZANDO AS EXPRESSÕES:
    print(f'-='*30)
    print(f'Resultado da expressão A: [(X < Y) AND (Y < Z)] {A}')
    print(f'-='*30)
    print(f'Resultado da expressão B: [(X > Y) AND (Y < Z)] {B}')
    print(f'-='*30)
    print(f'Resultado da expressão C: [(X < Y) OR (Y < Z)] {C}')
    print(f'-='*30)
    print(f'Resultado da expressão D: [(X < Y) OR (Y > Z)] {D}')
    print(f'-='*30)
    print(f'Resultado da expressão E: [(X > Y) OR (Y < Z)] {E}')
    print(f'-='*30)
    ContadorDaInterface =+ 1
    while True:
        continuar = input('Você deseja continuar no programa? [S/N]: ').upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print(f'Opção Inválida!')
    if continuar == 'N':
        break
FinalDoContadorDeTempo = time.time()
ConversaoParaTempoGasto = (FinalDoContadorDeTempo - InicioDoContadorDeTempo) / 60
print(f'[{ConversaoParaTempoGasto:.2f}] Tempo de execução do programa.')
