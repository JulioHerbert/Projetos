#Cálculo Poliedro:
while True:
    while True:
        try:
            vertices = int(input('Quantos vertices tem o poliedro? '))
            arestas = int(input('Quantas arestas tem o poliedro? '))
            break
        except ValueError:
            print('ERRO! Por favor digite apenas valores inteiros.')
    #Formula de Euler:
    calculo = (arestas * vertices) // 2
    formulaEuler = calculo - vertices + 2
    print('=='*40)
    print(f'Número de faces: {formulaEuler}')
    print('=='*40)
    while True:
        continuar = input('você deseja continuar no programa? [S/N]: ').upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção Inválida!')
    if continuar == 'N':
        break
print('Execução encerrada!')