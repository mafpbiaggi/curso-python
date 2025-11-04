'''
Desafio 51: https://youtu.be/cL4YDtFnCt4?t=1777
Correção: 

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
