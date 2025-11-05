'''
Desafio 63: https://youtu.be/LH6OIn2lBaI?t=1974
Correção: https://youtu.be/w7yn1_Mfu0E

Enunciado:
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os
n primeiros elementos de uma sequência de Fibanacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('======== Desafio 63 ========')
print('Exibe sequência de Fibonacci\n')

n = int(input('Digite o número de elementos a serem exibidos: '))
ant = 0
atual = 0
prox = 0

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
print()

'''
# Solução do professor:

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)
'''
