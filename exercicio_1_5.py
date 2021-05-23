"""
Faça um Programa que converta metros para centímetros.
"""
print('Converter Metro para Centímetro')
# Solicita que o usuário informe o valor a ser convertido e armazena o dado em uma variável
medida = float(input('Medida: '))
# Exibe a conversão calculando-a de forma direta
print(f'{medida:.2f} metro(s) equivale(m) a {medida * 100:.2f} centímetro(s).')
