'''
Desafio 96:  https://youtu.be/ezfr9d7wd_k?t=2503
Correção: 

'''
sub = 'Um print especial'

'''
Enunciado:
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.

Ex: escreva('Olá, Mundo!')
Saída:
    ~~~~~~~~~~~
    Olá, Mundo!
    ~~~~~~~~~~~
'''

def titulo(t, s):
    print('=' * 60)
    print(f'{t:^60}')
    print('-' * 60)
    print(f'{s:^60}')
    print('-' * 60)
    print()


titulo('Desafio 97', sub)
