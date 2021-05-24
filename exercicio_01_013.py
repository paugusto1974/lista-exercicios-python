"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Informe sua altura em metro: '))
pesoSeHomem = (72.7 * altura) - 58
pesoSeMulher = (62.1 * altura) - 44.7
print(f'Para quem tem {altura} m de altura, o peso ideal é\n'
      f'{pesoSeHomem:.2f} kg se for homem ou {pesoSeMulher:.2f} kg se for mulher.')
