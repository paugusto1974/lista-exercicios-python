"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Informe sua altura em metro: '))
pesoideal = (72.7 * altura) - 58
print(f'Se você tem {altura} m de altura, seu peso ideal são {pesoideal:.2f} kg.')
