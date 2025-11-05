'''
Desafio 62: https://youtu.be/LH6OIn2lBaI?t=1928
Correção:

Enunciado:
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('===== Desafio 62 ======')
print('Progressão Aritmética\n')

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

t = 1
f = 1
print('PA = ', end='')
while t != 0: 
    if f == 1:
        print('{} '.format(p+(f-1)*r), end='')
    else:
        t = int(input('Você deseja mostrar mais quantos elementos? '))
    f += 1

print('\n')


