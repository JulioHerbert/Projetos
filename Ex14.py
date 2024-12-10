###Considerando que na ETEMAC, temos dois cursos (RC e LOG).
###Faça um programa que leia a quantidade de alunos de cada
###turma/ano e mostre quantos são de Redes de computadores e
###quantos são de Logística junto com o total geral de alunos.

#INICÍO DO PROGRAMA:
TotalDeRedes = []
TotalDeLog = []
contador = 0
while True:
    if contador == 0:
        print(f'{"<<<CONTADOR DE ALUNO>>>":^{75}}\n')
    print("=="*40)
    print('LEVANTAMENTO DE DADOS DOS ALUNOS:\n')
    #(A) REDES DE COMPUTADORES:
    while True:
        try:
            TotalDeRedes.append(int(input('Digite a quantidade de alunos do [1º A Redes]: ')))
            TotalDeRedes.append(int(input('Digite a quantidade de alunos do [2º A Redes]: ')))
            TotalDeRedes.append(int(input('Digite a quantidade de alunos do [3º A Redes]: ')))
            #(B) LOGÍSTICA:
            print("--"*40)
            TotalDeLog.append(int(input('Digite a quantidade de alunos do [1º B Logística]: ')))
            TotalDeLog.append(int(input('Digite a quantidade de alunos do [2º B Logística]: ')))
            TotalDeLog.append(int(input('Digite a quantidade de alunos do [3º B Logística]: ')))
            break
        except ValueError:
            print(f'ERRO! digite somente números INTEIROS.')
    print()
    print("=="*40)
    print('DADOS DA QUANTIDADE GERAL DE ALUNOS:\n')
    print(f'Total de alunos no curso de [REDES DE COMPUTADORES]: {sum(TotalDeRedes)}')
    print(f'Total de alunos no curso de [LOGÍSTICA]: {sum(TotalDeLog)}')
    print(f'Total de alunos na escola [ETEMAC]: {sum(TotalDeRedes+TotalDeLog)}')
    print("=="*40)
    while True:
        continuar = input('você deseja reiniciar o programa? [S/N]: ').strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            TotalDeRedes.clear()
            TotalDeLog.clear()
            contador = contador + 1
            break
        print(f'Opção Inválida!')
    if continuar == 'N':
        break
print(f'Total de vezes executado: {contador}')




