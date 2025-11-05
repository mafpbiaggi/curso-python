'''
Desafio 63: https://youtu.be/LH6OIn2lBaI?t=1974
Correção:

Enunciado:
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os
n primeiros elementos de uma sequência de Fibanacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('======== Desafio 63 ========')
print('Exibe sequência de Fibonacci\n')

n = int(input('Digite o número de elementos a serem exibidos: '))
ant = atual = prox = 0

i = 1
while i <= n:
    if prox == 0:
        print('{}'.format(prox), end='')
        prox = 1
    else:
        print(' -> {}'.format(prox), end='')
        ant = atual
        atual = prox
        prox = ant + atual
    i += 1
print('\n')
