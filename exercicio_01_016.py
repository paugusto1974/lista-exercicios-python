"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
"""
# importa a função 'ceil' da biblioteca 'math'
from math import ceil
# Recebe dimensões das paredes e calcula o tamanho em metros quadrados
altura = float(input('Informe a LARGURA da parede em metro: '))
largura = float(input('Informe a ALTURA da parede em metro: '))
tamanho = altura * largura
# Calcula a quantidade de litros necessários para o serviço
litros = tamanho / 3
# Calcula quantos galoes deverão ser comprados; arredonda a quantidade para
# cima utilizando a função math.ceil(), já que não se vendem galões fracionados
galoes = ceil(litros / 18)
preco_galao = 80.00
preco_a_pagar = galoes * preco_galao
print(f'A parede mede {tamanho:.2f}m².\n'
      f'Litros necessários: {litros:.2f} litros.\n'
      f'Deverão ser comprados {galoes} galões a R$ {preco_galao} cada.\n'
      f'Custo total dos galões: R$ {preco_a_pagar:.2f}.')
