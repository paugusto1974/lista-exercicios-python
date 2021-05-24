"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
   + Salário Bruto : R$
   - IR (11%) : R$
   - INSS (8%) : R$
   - Sindicato ( 5%) : R$
   = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
hora_de_trabalho = float(input('Informe o valor da hora de trabalho: R$ '))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
salario_bruto = hora_de_trabalho * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato # soma todos os descontos
salario_liquido = salario_bruto - descontos
print(f'Salário Bruto: + R$ {salario_bruto:.2f}')
print(f'Total de Descontos: - R$ {descontos:.2f}')
print(f'A receber: R$ {salario_liquido:.2f}')
