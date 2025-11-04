'''
Desafio 51: https://youtu.be/cL4YDtFnCt4?t=1777
Correção: https://youtu.be/-OnqSGh0u4g

Enunciado:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiro termos dessa progressão.
'''

print('===== Desafio 51 ======')
print('Progressão Aritmética\n')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
f = p + (11 - 1) * r

print('PA = ( ', end='')
for i in range(p, f, r):
    print('{} '.format(i), end='')
print(')')

"""
# Solução do professor:

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * r
for c in range (primeiro, décimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
"""
