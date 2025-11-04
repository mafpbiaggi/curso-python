'''
Desafio 50: https://youtu.be/cL4YDtFnCt4?t=1753
Correção: https://youtu.be/rJaBLOW57Jg

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

"""
# Solução do professor:

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
"""
