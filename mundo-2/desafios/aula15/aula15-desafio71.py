"""
Desafio 71: https://youtu.be/1OFp_-R2B2A?t=2155
Correção:

Enunciado:"""
sub = ' Simulador de Caixa Eletrônico '
"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
"""
t_sub = int((52 - len(sub)) / 2)
print('=' * 19 + ' Desafio 71 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

print('\nSaque ' + '-' * 45)
print('Notas Disponíveis: R$ 50, R$ 20, R$ 10 e R$ 1')

n = int(input('\nQual valor deseja sacar? R$ '))
notas = [50, 20, 10, 1]

cont = 0
print('\nQuantidade de cédulas ' + '-' * 29)
while True:
    resto = n % notas[cont]
    t_ced = n // notas[cont]

    if t_ced > 0:
        print(f'{t_ced:2} de R$ {notas[cont]:2}.')
        if resto == 0:
            break

    n = resto
    cont += 1

print('\nVolte sempre ' + '=' * 38)
