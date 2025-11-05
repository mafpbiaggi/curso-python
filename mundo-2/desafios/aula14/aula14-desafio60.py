'''
Desafio 60: https://youtu.be/LH6OIn2lBaI?t=1838
Correção:

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
