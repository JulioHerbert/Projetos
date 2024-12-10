#Imprimindo os valores de 100 a 250:
print(f'\nValores de 100 a 250:')
for num in range(100, 251):
    print(f'{num}, ', end='')
#Imprimindo a soma de 1 até 100:
print(f'\n\nSoma de 1 até 100:')
soma = 0
for n1 in range(1, 101):
    soma += n1
print(f'A soma de 1 até 100 é: {soma}')
#imprimir todos os múltiplos de 5 entre 1 e 300:
print('\nMultiplos de 5 entre 1 e 300:')
for n2 in range(1, 301):
    if n2 % 5 == 0:
        print(f'{n2}, ', end='')
#Imprimindo a tabuada:
numeroTabuada = int(input('\n\nVocê quer saber a tabuada de qual número?: '))
print(f'<<< TABUADA DO NÚMERO {numeroTabuada} >>>')
print('=='* 40)
for temp in range(1, 11):
    print(f'{numeroTabuada} x {temp} = {numeroTabuada*temp}')
print('=='* 40)
#Imprimindo os números pares de 1 a 20:
ListaPar = []
ListaImpares = []
par = 0
impares = 0
cont = 1
for temp1 in range(1, 21):
    n3 = int(input(f'Digite o {cont}º número: '))
    cont += 1
    if n3 % 2 == 0:
        ListaPar.append(n3)
        par += 1
    else:
        ListaImpares.append(n3)
        impares += 1
print('=='* 40)
print(f'Tivemos um total de {par} números pares!')
print(f'Tivemos um total de {impares} números Ímpares!')
print('=='* 40)
print(f'Os números pares digitados foram: {ListaPar}')
print(f'Os números Ímpares digitados foram: {ListaImpares}')
print('=='* 40)
#Soma de números digitados:
soma = 0
while True:
    SequenciaDeNúmeros = int(input('Digite um número para sua soma ou [0 PARA PARAR O PROGRAMA]: '))
    if SequenciaDeNúmeros == 0:
        break
    else:
        soma += SequenciaDeNúmeros
print(f'A soma dos números digitados foram: {soma}')
print(f'Execução encerrada!')