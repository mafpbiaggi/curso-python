'''
Desafio 96: https://youtu.be/ezfr9d7wd_k?t=2445
Correção: https://youtu.be/oV1s53YGtvE

'''
sub = 'Função que calcula área'

'''
Enunciado: 
Faça um programa que tenha uma função chamada área(), que receba do usuário as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terrano.
'''

def titulo(t, s):
    print('=' * 60)
    print(f'{t:^60}')
    print('-' * 60)
    print(f'{s:^60}')
    print('-' * 60)
    print()

def area(l, c):
    a = l*c
    print(f'\nA área do terreno ({l:.2f}m x {c:.2f}m) é {a:.2f}m²')


titulo('Desafio 96', sub)
lar = float(input('Digite a largura do terreno (m): '))
com = float(input('Digite o comprimento do terreno (m): '))

area(lar, com)

'''
# Solução do professor:

def  área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print(' Controle de Terrenos')
print('-' * 20)
l = float(iinput('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
'''
