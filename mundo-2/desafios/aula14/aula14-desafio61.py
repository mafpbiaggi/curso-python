'''
Desafio 61: https://youtu.be/LH6OIn2lBaI?t=1894
Correção: https://youtu.be/vu5ehetQGe8

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
while f <= 10: 
    print('{} '.format(p+(f-1)*r), end='')
    f += 1
print(')')

'''
# Solução do professor:

print('Gerado de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
'''
