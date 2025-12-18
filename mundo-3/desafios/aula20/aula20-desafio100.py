'''
Desafio 100: https://youtu.be/ezfr9d7wd_k?t=2888
Correção: https://youtu.be/MEs-41JcuhM

'''
sub = 'Funções para sortear e somar'

'''
Enunciado:
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.
'''

from time import sleep
from random import randint


def sorteia(num):
    print('\nSorteando 5 números entre 1 e 20 ...', end=' ')
    for c in range (0, 5):
        n = randint(1, 20)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
        num.append(n)
    print()

def somaPar(num):
    s = 0
    for n in num:
        if n % 2 == 0:
            s += n
    print(f'A soma dos valores pares contidos em {num}, é {s}.')


print('=' * 60)
print(f'{"Desafio 100":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

numeros = list()
sorteia(numeros)
somaPar(numeros)

'''
# Solução do professor:
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)

'''