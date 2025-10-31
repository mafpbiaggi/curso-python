# Desafio 38: https://youtu.be/j9bYDjaAYzw?t=1181
# Correção: https://youtu.be/iuPbB9uHczM

# Enunciado:
'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.'''

print('====== Desafio 38 ======\n')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\nO primeiro valor é maior: {} > {}'.format(n1, n2))
elif n2 > n1:
    print('\nO segundo valor é maior: {} > {}'.format(n2, n1))
elif n1 == n2: # Esse comando poderia ser somente else:
    print('\nNão existe valor maior: {} = {}'.format(n1, n2))

'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 < n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
'''
