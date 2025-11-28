'''
Desafio 99: https://youtu.be/ezfr9d7wd_k?t=2780 
Correção: 

'''
sub = 'Função que descobre o maior'

'''
Enunciado:
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior.

Obs: Os valores são adicionados diretamente no programa, sem digitação de valores pelo usuário.
Caso não haja parâmetros, a função retorna 0 como maior valor.
Usar o flush para a função sleep (Vide exercício do Joken Pô).
'''
from time import sleep

def loading():
    for i in range(0, 3):
        print('.', end='', flush=True)
        sleep(0.5)
    print(end=' ')

def maior(* param):
    m = 0
    l_param = len(param)
    if l_param > 0:
        m = max(param)
    
    print('\nAnalisando os valores passados', end=' ')
    loading()

    for p in param:
        print(f'{p}', end=' ', flush=True)
        sleep(0.5)

    print(f'\nForam informados {l_param} valores no total', end = ' ')
    loading()

    print(f'\nO maior valor entre eles é {m}.')
    print('-' * 60)
    sleep(1.5)


print('=' * 60)
print(f'{"Desafio 99":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

maior(15, 34, 17, 2, 3)
maior(2, 9, 4, 5, 7, 1)
maior(4, 0, 7)
maior(1, 2)
maior(2000,1)
maior()
