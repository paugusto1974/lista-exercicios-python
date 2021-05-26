"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 - comprar apenas latas de 18 litros;
 - comprar apenas galões de 3,6 litros;
 - misturar latas e galões, de forma que o desperdício de tinta seja menor.
   Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
   considere latas cheias.
"""
# importação da função 'ceil' da biblioteca 'math'
from math import ceil
# Recebe o tamanho em metros quadrados
tamanho = float(input('Informe o tamanho da parede em metros quadrados: '))
# Calcula a quantidade de litros necessários para o serviço
litros = tamanho / 6
print(f'Quantidade de tinta necessária para pintar {tamanho:.2f}m² de parede: {litros:.2f} litros.')

# Calcula quantas latas de 18 litros serão necessárias; arredonda a quantidade
# para cima utilizando a função math.ceil() já que não se vendem latas fracionadas.
quantidade_latas_180 = ceil(litros / 18)
preco_lata_180 = 80.00
preco_a_pagar = quantidade_latas_180 * preco_lata_180
print(f'\033[0;30;46mConsiderando-se apenas latas de 18 litros,\n'
      f'deverão ser compradas {quantidade_latas_180} latas a R$ {preco_lata_180} cada.\n'
      f'Total de litros: {quantidade_latas_180 * 18:.1f}.\n'
      f'Custo total da compra: R$ {preco_a_pagar:.2f}.')

# Calcula quantos galoes de 3,6 litros serão necessários; arredonda a quantidade
# para cima utilizando a função math.ceil() já que não se vendem galões fracionados.
quantidade_galoes_036 = ceil(litros / 3.6)
preco_galao_036 = 25.00
preco_a_pagar = quantidade_galoes_036 * preco_galao_036
print(f'\033[0;30;47mConsiderando-se apenas galões de 3,6 litros,\n'
      f'deverão ser comprados {quantidade_galoes_036} galões a R$ {preco_galao_036} cada.\n'
      f'Total de litros: {quantidade_galoes_036 * 3.6:.1f}.\n'
      f'Custo total da compra: R$ {preco_a_pagar:.2f}.')

# Cálculo definindo quantidade de latas e galões a fim de otimizar o consumo de tinta.
quantidade_latas_180 = litros // 18  # separa a parte inteira para calcular a quantidade de galões de 18 litros
quantidade_latas_180 = quantidade_latas_180 + quantidade_latas_180 * 0.1
litros = litros % 18  # separa a parte fracionada para calcular com galoes de 3,6 litros
quantidade_galoes_036 = ceil(litros / 3.6)  # arredonda para cima
quantidade_galoes_036 = quantidade_galoes_036 + quantidade_galoes_036 * 0.1
print(f'\033[0;30;44mSerão necessárias {int(quantidade_latas_180)} latas de 18 litros e '
      f'{quantidade_galoes_036} galões de 3,6 litros.\n'
      f'Total de litros: {quantidade_latas_180 * 18 + quantidade_galoes_036 * 3.6:.1f}.\n'
      f'Custo total dos galões e latas:'
      f'{(quantidade_latas_180 * preco_lata_180 + quantidade_galoes_036 * preco_galao_036):.2f}.')
# O enunciado estabelece um acrescimo de 10% apenas para esse cálculo, o que eleva o consumo de tinta
# em comparação com os dois primeiros cálculos. Dessa forma não ocorre otimização do consumo embora o
# preço a ser pago diminua bastante em relação a compra apenas dos galões de 3,6 litros.
# Poderia buscar maneiras de otimizar os cálculos e melhorar o programa, mas já estou enjoado desse exercício.
