'''
Desafio 97:  https://youtu.be/ezfr9d7wd_k?t=2503
Correção: https://youtu.be/Q6basnSo7r0

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

def escreva(txt):
    f_len = len(txt) + 10

    print()
    print('~' * f_len)
    print(f'{txt:^{f_len}}')
    print('~' * f_len)


titulo('Desafio 97', sub)
escreva(str(input('Digite um texto qualquer: ')).strip())

'''
# Solução do professor:

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
'''
