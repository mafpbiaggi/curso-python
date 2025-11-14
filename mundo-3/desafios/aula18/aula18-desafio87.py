'''
Desafio 87: https://youtu.be/YV_JQmZNFsk?t=1763
Correção: https://youtu.be/QhS829x6up4

Enunciado:'''
sub = ' Matriz em Python 2.0 '

'''Aprimore o desafio 86, mostrando no final:

a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 85 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

m = [[],[],[]]
soma_par = 0
soma_3col = 0
maior_2lin = 0

print()
for i in range (0, 3):
    for j in range(0, 3):
        n = (int(input(f'Digite o valor para [{i}][{j}]: ')))
        m[i].append(n)
        
        if n % 2 == 0:
            soma_par += n

print('\n' + '-' * 52)
print('Matriz\n')
for l in m:
    print(f'[{l[0]:^5}][{l[1]:^5}][{l[2]:^5}]')
print('\n' + '-' * 52)

for l in m:
    soma_3col += l[2]

for c in range(0, 3):
    if m[1][c] > maior_2lin:
        maior_2lin = m[1][c]
        
print(f'\nA soma dos números pares é {soma_par}.')
print(f'A soma dos valores da 3ª coluna é {soma_3col}.')
print(f'O maior número da 2ª linha é {maior_2lin}')


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}{c}]: '))

'''
# Solução do professor:

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda coluna é {mai}')
'''
