'''
Desafio 61: https://youtu.be/LH6OIn2lBaI?t=1894
Correção:

Enunciado:
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
'''

print('===== Desafio 61 ======')
print('Progressão Aritmética\n')

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

f = 1
print('PA = ( ', end='')
while f < 11: 
    print('{} '.format(p+(f-1)*r), end='')
    f += 1
print(')')
