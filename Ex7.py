DadosFuncionarios = []
from datetime import datetime
cont = 1
while True:
    Nome = str(input('Digite seu nome: ')).strip()
    HorasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
    ValorDaHora = float(input('Digite o valor da hora: '))
    PercentualAumento = float(input('Digite o percentual de aumento: '))
#Calculo da questão:
    SalarioFuncionario = (HorasTrabalhadas * ValorDaHora)
    AumentoSalario = (SalarioFuncionario * (PercentualAumento / 100))
    NovoSalario = (SalarioFuncionario + AumentoSalario)
#Adicionando os Dicionarios na Lista:
    DadosFuncionarios.append({"Nome": Nome, "HorasTrabalhadas": HorasTrabalhadas, "ValorDaHora": ValorDaHora,
                            "PercentualDeAumento": PercentualAumento, "SalarioFuncionario": SalarioFuncionario,
                            "AumentoSalario": AumentoSalario, "NovoSalario": NovoSalario
    })
    while True:
        continuar = str(input('Deseja continuar com o programa? [S/N]: ')).upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
        print(f'Opção inválida!')
    if continuar == 'N':
        break
#INTERFACE:
    print(f'Usuário Adicionado!')
print(f'-='*30)
for temp in DadosFuncionarios:
    print(f'{cont}º {temp["Nome"]}, seu salário é: R$: {temp["NovoSalario"]:.2f}')
    print(f'-='*30)
    print(f'Informações Adicionais do Funcionario:\n\nHoras Trabalhadas: {temp["HorasTrabalhadas"]}')
    print(f'Valor da Hora: {temp["ValorDaHora"]}\nPercentual de Aumento: {temp["PercentualDeAumento"]:.2f}%\n')
    print(f'-='*30)
    cont = cont + 1
print(f'Total de pessaos inscritas no programa: {len(DadosFuncionarios)}')
datahora = datetime.now()
print(f'Data e Hora: {datahora}')
