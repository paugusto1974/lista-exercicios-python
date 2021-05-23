"""
Faça um Programa que peça dois números e imprima a soma.
"""
# Exibe uma mensagem a fim de informar ao usuário o que o programa irá fazer
print('-=# Vamos Somar Dois Números #=-')
# Solicita dois números inteiros
n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe mais um número inteiro: '))
# Exibe na tela os números somados de forma direta
print(f'A soma dos dois números é {n1 + n2}')
# Em vez disso, a soma dos dois números pode ser armazenada em uma variável...
soma = n1 + n2
# E exibida ou utilizada da forma que for mais conveniente
print(f'{n1} + {n2} = {soma}')
