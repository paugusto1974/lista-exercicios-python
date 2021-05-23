"""
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
# Forma mais básica...
# Solicita que o usuário informe um número
numero = input('Informe um número: ')
# Exibe o número na tela utilizando 'print'
print(f'O número informado foi {numero}.')
# Forma um pouco melhor...
# Solicita que o usuário informe um número e já define-o como número inteiro
numero = int(input('Informe um número inteiro: '))
print(f'O número inteiro informado foi {numero}')
