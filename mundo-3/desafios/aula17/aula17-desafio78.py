'''
Desafio 78: https://youtu.be/N1hTsbW50eM?t=1678
Correção: https://youtu.be/q8Z1cRdJnfk

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

print(f'\nVocê digitou os números: {lista}')
print(f'O maior valor digitado foi {maior} nas posições: {lista.index(maior)}', end='')
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

'''
# Solução do professor:

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para o Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print('{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
'''
