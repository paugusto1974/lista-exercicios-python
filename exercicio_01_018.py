"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps),  calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
"""
tamanho_download = float(input('Informe o tamanho do arquivo a ser baixado (em MB): '))
velocidade_link = float(input('Informe a velocidade do link (em Mbps): '))
tempo_download = tamanho_download / velocidade_link
print(f'Tempo estimado para baixar o arquivo: {tempo_download:.2f} minutos.')
