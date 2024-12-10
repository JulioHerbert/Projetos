import time
lista_users = []
cont = 1
while True:
    nome_user = (str(input('Nome: ')).strip())
    parcela = float(input('digite o valor da parcela: R$ '))
    valor_pago = float(input('digite o valor pago: R$ '))
    juros_pagos = (valor_pago - parcela)
    percentual = (juros_pagos / parcela) * 100
    lista_users.append({"Nome": nome_user, "Parcela": parcela,
                        "ValorPago": valor_pago, "JurosPagos": juros_pagos,
                        "Percentual": percentual,
})
    while True:
        continuar = input('Quer continuar [S/N]? ').upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print(f'ERRO!')
    if continuar == 'N':
        break
for temp in lista_users:
    print(f'{cont}º Nom: {temp["Nome"]}\nJuros Pagos: R$ {temp["JurosPagos"]}\nPercentual de Juros: {temp["Percentual"]}%')
    cont = cont + 1
    print(f'-='*30)
Tot_Juros = sum(temp["JurosPagos"] for temp in lista_users)
MediaJuros = Tot_Juros / len(lista_users)
Tot_Percentual = sum(temp["Percentual"] for temp in lista_users)
MediaPercentual = Tot_Percentual / len(lista_users)
print(f'Salvando.')
time.sleep(1)
print(f'Salvando..')
time.sleep(1)
print(f'Salvando...')
time.sleep(1)
print(f'--'*30)
print(f'Informações extras: ')
print(f'Total de pessoas cadastradas no programa: {len(lista_users)}')
print(f'Média do Total de Juros: {MediaJuros}%')
print(f'Média do Percentual do total dos inscritos: {MediaPercentual}%')