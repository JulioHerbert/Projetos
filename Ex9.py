ListaDosCirculos = []
cont = 1
ContadorDeRaio = 0
while True:
    Raio = float(input('Digite o raio do círculo: '))
    CalculoAreaDoCirculo = 3.14 * (Raio * Raio)
    ListaDosCirculos.append({"Raio": Raio, "CalculoAreaDoCirculo": CalculoAreaDoCirculo,           
})
    while True:
        continuar = input('você deseja continuar? [S/N]: ').strip().upper()[0]
        if continuar == "S" or continuar == "N":
            break
        print(f'\033[31mERRO! Por favor digite somente [S] OU [N].\033[m')
    if continuar == 'N':
        break
for temp in ListaDosCirculos:
    print(f'-='*40)
    print(f'\033[1;97m{cont}º Círculo:\nRAIO: {temp["Raio"]:.2f}\nÁREA: {temp["CalculoAreaDoCirculo"]:.2f}')
    cont = cont + 1
SomaDosRaio = sum(temp["Raio"] for temp in ListaDosCirculos)
SomaDaArea = sum(temp["CalculoAreaDoCirculo"] for temp in ListaDosCirculos)
for temp1 in ListaDosCirculos:
    if temp1["Raio"] == 10:
        ContadorDeRaio = ContadorDeRaio + 1
print(f'-='*40)
print(f'Total de Cálculos Realizados: {len(ListaDosCirculos)}')
print(f'Total de raio igual a 10: {ContadorDeRaio}')
print(f'Média dos raios de todos círculos: {SomaDosRaio / len(ListaDosCirculos):.2f}')
print(f'Média da área dos círculos: {SomaDaArea / len(ListaDosCirculos):.2f}')




