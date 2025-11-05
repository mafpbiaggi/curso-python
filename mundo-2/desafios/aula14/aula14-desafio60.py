'''
Desafio 60: https://youtu.be/LH6OIn2lBaI?t=1838
Correção: https://youtu.be/9dlBZlkvvxY

Enunciado:
Faça um programa que leia um núemro qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''

print('====== Desafio 60 ======')
print('=== Fatorial ===\n')

n = int(input('Digite um número inteiro (>0): '))
print('{}! ='.format(n), end=' ')

fat = 1
while n > 0:
    fat *= n

    if n != 1:
        print('{}'.format(n), end='x')
    else:
        print('{}'.format(n), end=' ')
    n -= 1

print('= {}'.format(fat))

"""
# Soluções do professor:

a) Utilizando módulo
    from math import factorial
    n = int(input('Digite um número para calcular seu Fatorial: '))
    f = factorial(n)
    print('O fatorial de {} é {}'.format(n, f))

b) Utilizando laço
    n = int(input('Digite um número para calcular seu Fatorial: '))
    c = n
    f = 1
    print('Calculando {}! = '.format(n), end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print('{}'.format(f))
"""
