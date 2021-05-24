"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
A=πR²
P=2πR
"""
# Importa da biblioteca de funções matemáticas apenas a função 'pi' que já fornece o valor
from math import pi
print('Vamos calcular a ÁREA de uma circunferência supondo valores em METRO.')
# Recebe o valor do RAIO
raio = float(input('Informe a medida do raio: '))
# Calcula a área e armazena o valor em uma variável
area = pi * raio ** 2
# Exibe na tela o valor da circunferência
print(f'A circunferência mede {area:.2f} m² de ÁREA;')
# Aproveitando o ensejo para calcular e exibir o perímetro de forma direta
print(f'E {2 * pi * raio:.2f} m é seu PERÍMETRO.')
