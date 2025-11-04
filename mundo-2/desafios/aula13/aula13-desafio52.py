'''
Desafio 52: https://youtu.be/cL4YDtFnCt4?t=1824
Correção:

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
