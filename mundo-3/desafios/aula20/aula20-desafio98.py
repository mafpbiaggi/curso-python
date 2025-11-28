'''
Desafio 98: https://youtu.be/ezfr9d7wd_k?t=2571
Correção: 

'''
sub = 'Função de contador'

'''
Enunciado:
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo.
Realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Um contagem personalizada.
'''

def titulo(t, s):
    print('=' * 60)
    print(f'{t:^60}')
    print('-' * 60)
    print(f'{s:^60}')
    print('-' * 60)
    print()


titulo('Desafio 98', sub)
