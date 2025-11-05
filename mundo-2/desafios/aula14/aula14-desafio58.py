'''
Desafio 58: https://youtu.be/LH6OIn2lBaI?t=1707
Correção: https://youtu.be/-QkOIHJ1Chw

Enunciado:
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só
que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

from random import randint
print('====== Desafio 28 ======')

n = randint(0, 10)
r = int(input('Hm .... Em qual número (de 0 a 10) eu estou pensando? '))

c = 1
while r != n:
    r = int(input('Você errou! Tente novamente: '))
    c += 1

print('\nParabéns! Você acertou. Eu pensei no número {}'.format(n))
print('Quantidade de tentativas: {}.'.format(c))

"""
# Solução do professor:

from random import randint
computador = randint(0, 10)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""
