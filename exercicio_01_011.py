"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""
a = int(input('Informe um valor inteiro: '))
b = int(input('Informe mais um valor inteiro: '))
c = float(input('Informe um valor real: '))
print(f'O dobro de {a} multiplicado pela metade de {b} é igual a {(2 * a) * (b / 2):.2f}')
print(f'O triplo de {a} somado com {c} é igual a {3 * a + c:.2f}')
print(f'O valor de {c} elevado à terceira é {c ** 3}')
