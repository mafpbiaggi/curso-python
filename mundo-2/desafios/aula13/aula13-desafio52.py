'''
Desafio 52: https://youtu.be/cL4YDtFnCt4?t=1824
Correção: https://youtu.be/Er5Hyd4LyVw

Enunciado:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

print('====== Desafio 52 ======')
print('Checagem de número primo')

cor = {'0':'\033[m',
       'vm':'\033[31m',
       'vd':'\033[32m',
       'b':'\033[1m'}

n = int(input('Digite um número inteiro: '))
c = 0

for i in range(1,n+1):
    if n % i == 0:
        c += 1

if c == 2:
    print('{}O número {} é primo.{}'.format(cor['vd'], n, cor['0']))
else:
    print('{}O número {} não é primo.{}'.format(cor['vm'], n, cor['0']))

"""
# Solução do professor:
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!.')
else:
    print('E por isso ele NÃO É PRIMO!')
"""
