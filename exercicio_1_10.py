"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
celsius = float(input('Informe a temperautura em graus CELSIUS: '))
fahrenheit = celsius * 1.8 + 32
print(f'{celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.')
