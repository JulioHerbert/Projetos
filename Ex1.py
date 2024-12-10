curso = list()
cont = 1
curso1 = 0
quant = int(input('quantos cursos a instituição possui? '))
while True:
    for c in range(0,quant):
        curso1 = int(input(f'Digite a quantidade de alunos do curso {cont}º: '))
        curso.append(curso1)
        cont = cont + 1
        soma = sum(curso)
    while True:
        conti = str(input('Você deseja continuar com o programa? [S] ou [N] ')).upper().strip()
        if conti == 'S' or conti == 'N':
            break
        print('Por favor digite somente [S] ou [N]')
    if conti == 'N':
        break
print(f'Total de alunos somandos os {quant} cursos: {soma}')
print('PROGRAMA ENCERRADOteste.')


    
