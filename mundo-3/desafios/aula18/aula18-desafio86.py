'''
Desafio 86: https://youtu.be/YV_JQmZNFsk?t=1673
Correção:

Enunciado:'''
sub = ' Matriz em Python '
'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

Ex: Digite um valor para [0, 0]: 
    Digite um valor para [0, 1]:
    Digite um valor para [0, 2]: ...
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 85 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

m = [[],[],[]]

print()
for i in range (0, 3):
    for j in range(0, 3):
        m[i].append(int(input(f'Digite o valor para [{i}][{j}]: ')))

print('\n' + '-' * 52)
print('Matriz\n')
for l in m:
    print(f'[{l[0]:^5}][{l[1]:^5}][{l[2]:^5}]')
print('\n' + '-' * 52)
