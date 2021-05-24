"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
# Informa o propósito do programa
print('Informe as 4 notas bimestrais do aluno para calcular a Média: ')
# Solicita as notas e armazena-as em quatro variáveis
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
nota3 = float(input('Terceira Nota: '))
nota4 = float(input('Quarta Nota: '))
# Cacula a média armazenando-a em uma nova variável
media = (nota1 + nota2 + nota3 + nota4) / 4
# Exibe a Média na tela com uma casa após o ponto flutuante
print(f'O aluno obteve média {media:.1f}.')
# Agora o cálculo da Média Ponderada com as mesmas notas
media = (nota1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / 10
# Exibe a Média Ponderada
print(f'Média ponderada com as mesmas notas: {media:.1f}.')
