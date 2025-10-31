# Desafio 37: https://youtu.be/j9bYDjaAYzw?t=1091
# Correção: https://youtu.be/B3F0IjH5WAM

# Enunciado:
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print('====== Desafio 37 ======\n')

cor = {'0':'\033[m',
       'vd':'\033[32m',
       'am':'\033[33m',
       'az':'\033[34m',
       'b':'\033[1m'}

n = int(input('Digite um número inteiro: '))
x = int(input('Escolha a base de conversão\n{}1: Binário\n{}2: Octal\n{}3: Hexadecimal{}: '.format(cor['vd'], cor['az'], cor['am'], cor['0'])))

if x == 1:
    print('\nNúmero: {} => Binário: {}'.format(n, bin(n)))
elif x == 2:
    print('\nNúmero: {} => Octal: {}'.format(n, oct(n)))
elif x == 3:
    print('\nNúmero: {} => Hexadecimal: {}'.format(n, hex(n)))
else:
    print('\nOpção inválida ({}). Tente novamente.'.format(x))

"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida, tente novamente.')
"""
