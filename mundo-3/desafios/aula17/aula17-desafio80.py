'''
Desafio 80: https://youtu.be/N1hTsbW50eM?t=1897
Correção:

Enunciado:'''
sub = ' Lista ordenada sem repetições '
'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()), mostrando em qual posição ele foi inserido.

No final, mostre a lista ordenada na tela.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 80 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

lista = []
for i in range(1, 6):
    n = int(input(f'\nDigite o {i}º número: '))
    
    if i == 1:
        lista.append(n)
        print('Número inserido no final da lista.')
    else:
        for j in range(len(lista)):
            if n < lista[j]:
                lista.insert(j, n)
                print(f'Número inserido na posição {j}.')

print(lista)