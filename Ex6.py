Regiao = []
cont = 1
while True:
    NomeRegiao = str(input('Qual região? '))
    QuantiApartamento = int(input('Digite a quantidade de apartamentos: '))
    ValorContaEnergia = float(input('Digite o valor da conta de energia: R$ '))
    ValorContaAgua = float(input('Digite o valor da conta de água: R$ '))
    TotValor = (ValorContaAgua + ValorContaEnergia)
    ValorMorador = (TotValor / QuantiApartamento)
    Percentual = (ValorMorador / TotValor) * 100
    Regiao.append({"Região": NomeRegiao, "ValorTotal": TotValor, "Percentual": Percentual,
                   
})
    continuar = str(input('você deseja continuar? [S/N]: ')).upper().strip()
    while True:
        if continuar == 'S' or continuar == 'N':
            break
            print(f'Opção Inválida!')
    if continuar == 'N':
        break
print(f'-='*40)
for variaveltemp in Regiao:
    print(f'{cont}º Região: {variaveltemp["Região"]}\nValor Total que cada morador deve pagar: R$ {variaveltemp["ValorTotal"]:.2f}\nPercentual que cada morador deve pagar: R$ {variaveltemp["Percentual"]:.2f}%')
    cont += 1
    print(f'-='*40)