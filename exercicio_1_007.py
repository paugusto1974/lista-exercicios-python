"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
# Recebe o valor digitado e coloca-o em uma variável
medida = float(input('Informe a medida do lado de um quadrado: '))
# Calcula a área do quadrado utilizando o operador de potência
print(f'Sua área mede {medida ** 2:.2f} unidades.')
# Calcula a área utilizandoa a função 'pow' e depois multiplica o
# resultado por 2 a fim de obter o dobro da área conforme enunciado
print(f'O dobro da área do quadrado mede {pow(medida, 2) * 2:.2f} unidades.')
