ListaDeCandidatos = []
ListaDeVotos = []
while True:
    while True:
        Nome = str(input('Qual é o nome do candidato?: '))
        if not Nome.isalpha():
            print('ERRO! Por favor digite apenas letras.')
        else:
            break
    while True:
        try:
            Votos = int(input(f'Quantos votos o candidato {Nome} obteve?: '))
            break
        except ValueError:
            print('ERRO! Por favor digite apenas valores inteiros.')
    ListaDeCandidatos.append({"NOME": Nome})
    ListaDeVotos.append(Votos)
    Vencedor = ListaDeVotos.index(max(ListaDeVotos))
    while True:
        continuar = str(input('\nDeseja adicionar mais um candidatos? [S/N]: ')).upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção inválida!')
    if continuar == 'N':
        break
print('=='*40)
print(f'VENCEDOR DA ELEIÇÃO: {ListaDeCandidatos[Vencedor]["NOME"]}')
print('=='*40)