'''
Desafio 74: https://youtu.be/0LB3FSfjvao?t=2781
Correção: https://youtu.be/mlwt2CRQkTQ

Enunciado:'''
sub = ' Maior e menor valores em Tupla '

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 74 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

tup = ()
print('\nOs números inteiros gerados foram:', end=' ')
for i in range(0, 5):
        n = randint(1,10)
        tup += n,
        print(n, end=' ')

print(f'\nO conteúdo da tupla é {tup}')
print(f'O maior valor presente na tupla é {max(tup)}.') # Corrigido com utilização de max() e min().
print(f'O menor valor presente na tupla é {min(tup)}.')

"""
# Solução do professor:

from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
"""
