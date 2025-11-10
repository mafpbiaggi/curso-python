'''
Desafio 75: https://youtu.be/0LB3FSfjvao?t=2841
Correção:

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

if tup.count(3) > 0:
    print(f'A primeira ocorrência do número 3 está na posição {tup.index(3)}')
else:
    print(f'\033[33mO número 3 não foi inserido pelo usuário.\033[m')

print('Os números pares digitados foram: ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')
print()
