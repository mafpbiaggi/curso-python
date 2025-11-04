'''
Desafio 50: https://youtu.be/cL4YDtFnCt4?t=1753
Correção:

Enunciado:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor for ímpar, desconsidere-o.
'''

print('====== Desafio 50 ======')

s = 0
for i in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma dos número pares digitados é: {}.'.format(s))
