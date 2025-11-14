'''
Desafio 88: https://youtu.be/YV_JQmZNFsk?t=1863
Correção:

Enunciado:'''
sub = ' Mega Sena '
'''Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

Obs: Não pode haver repetição de número dentro do mesmo jogo (palpite).
'''
from time import sleep
from random import randint

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 85 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

palpites = list()
jogo = list()

n = int(input('\nQuantos jogos você quer gerar? '))

for i in range(0, n):
    for j in range(0, 6):
        n_temp = '{:02}'.format(randint(1, 60))
        while n_temp in jogo:
            n_temp = '{:02}'.format(randint(1, 60))
    
        jogo.append(n_temp)
    
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()

print('-' * 52)
for c, p in enumerate(palpites):
    print(f'Jogo {c+1:>2}: {p}')
    sleep(1.25)
print('-' * 52)
