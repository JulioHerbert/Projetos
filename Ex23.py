candidatos = []
while True:
    for i in range(3):
        candidatos.append(int(input(f'Qual o total de votos do candidato {i+1}º ? ')))
    if candidatos[0] > (candidatos[1] + candidatos[2]):
        print(f'Não havera segundo turno, pois candidato 1 obteve mais votos.')
    elif candidatos[1] > (candidatos[0] + candidatos[2]):
        print(f'Não havera segundo turno, pois candidato 2 obteve mais votos.')
    elif candidatos[2] > (candidatos[0] + candidatos[1]):
        print(f'Não havera segundo turno, pois candidato 3 obteve mais votos.')
    else:
        print(f'Haverá segundo turno')
    candidatos.clear()
    while True:
         continuar = input('você deseja continuar no programa? [S/N]: ').strip().upper()[0]
         if continuar == 'S' or continuar == 'N':
              break
         print('Opção Inválida!')
    if continuar == 'N':
         break
print('Execução encerrada!')
