"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
# Solicita o valor da hora de trabalho e o total de horas trabalhadas
# no mês e armazena os dados nas respectivas variáveis
hora_trabalho = float(input('Quanto você ganha por hora de trabalho: R$ '))
horas_trabalhadas = float(input('Quantidade de horas trabalhadas no mês: '))
# Exibe o resultado multiplicando um valor pelo outro
print(f'Seu pagamento será R$ {hora_trabalho * horas_trabalhadas:.2f}.')
