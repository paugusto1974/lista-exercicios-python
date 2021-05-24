"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
fahrenheit = float(input('Informe a temperautura em graus FAHRENHEIT: '))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f'{fahrenheit:.1f}°F corresponde a {celsius:.1f}°C.')
