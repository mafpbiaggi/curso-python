'''
Desafio 75: https://youtu.be/0LB3FSfjvao?t=2841
Correção: https://youtu.be/1u7oA8ckjAc

Enunciado:'''
sub = ' Análise de Dados em Tupla '

'''Desenvolva um programa que leia quatro valores e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.

Observação: Inserão de números 1 por 1.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 75 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub + '\n')

tup = ()
for i in range(0, 4):
    tup += int(input('Digite um número inteiro (entre 0 e 10): ')),

print(f'\nO número 9 aparece {tup.count(9)} vezes na tupla.')

if 3 in tup: # Corrigido usando menos recursos.
    print(f'A primeira ocorrência do número 3 está na posição {tup.index(3)}')
else:
    print(f'\033[33mO número 3 não foi inserido pelo usuário.\033[m')

print('Os números pares digitados foram: ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')
print()

"""
# Solução do professor:

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
"""
