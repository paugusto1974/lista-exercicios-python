"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável 'peso' (peso de peixes) e calcule o excesso.
Gravar na variável 'excesso' a quantidade de quilos além do limite e na variável 'multa' o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input('Informe o peso total do pescado em quilos: '))
excesso = peso - 50
# O ideal para essa tarefa seria criar uma codição que não efetuasse o cálculo da multa
# em casos em que não houvesse excesso de pescado. Entretanto o tópico não é abordado
# nessa série de exercícios, tanto é que não foi solicitado no enunciado.
multa = excesso * 4
print(f'Foram pescados {excesso:.2f} kg além do limite.\n'
      f'Multa devida: R$ {multa:.2f}')
