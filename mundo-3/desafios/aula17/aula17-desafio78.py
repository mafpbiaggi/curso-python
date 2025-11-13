'''
Desafio 78: https://youtu.be/N1hTsbW50eM?t=1678
Correção:

Enunciado:'''
sub = ' Maior e menor valores na lista '

'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
na lista.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 78 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)
lista = []

print()
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor [{i}]: ')))

maior = max(lista)
menor = min(lista)

print(f'\nO maior valor digitado foi {maior} nas posições: {lista.index(maior)}', end='')
if lista.count(maior) > 1:
    for n in range(lista.index(maior)+1,len(lista)):
        if lista[n] == maior:
            print(f', {n}', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: {lista.index(menor)}', end='')
if lista.count(menor) > 1:
    for n in range(lista.index(menor)+1,len(lista)):
        if lista[n] == menor:
            print(f', {n}', end='')
print()
