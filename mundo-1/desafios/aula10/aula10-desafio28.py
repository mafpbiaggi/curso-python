# Desafio 28: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1654
# Correção: https://youtu.be/kchC5KLZSZ4?si=9yqC90lu6Q5Oxib4

# Enunciado:
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
print('====== Desafio 28 ======')

r = int(input('Hm .... Em qual número (de 0 a 5) eu estou pensando? '))
n = choice([0, 1, 2, 3, 4, 5])

if  r == n:
    print('Você ganhou! Parabéns. ({}:{})'.format(n, r))
else:
    print('Você perdeu! ({}:{})'.format(n, r))


# Solução do professor:
'''
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''
