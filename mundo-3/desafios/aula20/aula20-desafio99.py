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

def titulo(t, s):
    print('=' * 60)
    print(f'{t:^60}')
    print('-' * 60)
    print(f'{s:^60}')
    print('-' * 60)
    print()


titulo('Desafio 99', sub)
