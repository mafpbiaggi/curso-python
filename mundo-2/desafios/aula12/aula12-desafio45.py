"""
Desafio 45: https://youtu.be/j9bYDjaAYzw?t=1517
Correção: https://youtu.be/tapTa6KVG-A

Enunciado:
Crie um programa que faça o computador jogar jokenpô com você.
"""

from random import choice
from time import sleep

print('-=-' * 15)
print('{:^45}'.format('Desafio 45 ==== Jokenpô'))
print('-=-' * 15)

cor = {'0':'\033[m',
       'vm':'\033[31m',
       'vd':'\033[32m',
       'am':'\033[33m',
       'b':'\033[1m'}

cpu = str(choice(['Pedra', 'Papel', 'Tesoura']))
jg1 = str.title(input('Vocẽ escolhe Pedra, Papel ou Tesoura? ')).strip()

# Valida a entrada do jogador 1
if jg1 != 'Pedra' and jg1 != 'Papel' and jg1 != 'Tesoura':
    print('{}\nInsira uma opção válida{}'.format(cor['am'], cor['0']))

else:
    print('\n{}Jokenpô{} ...'.format(cor['b'], cor['0']), end = " ")
    sleep(0.5)
    print('Computador: {} | Você: {}\n'.format(cpu, jg1))
    sleep(1)

        
    if cpu == jg1:
        print('{}Deu empate!{}'.format(cor['am'], cor['0']))

    else:
        if cpu == 'Pedra':
            if jg1 == 'Tesoura':
                print('{}{} vence {}. Você perdeu!{}'.format(cor['vm'], cpu, jg1, cor['0']))
            elif jg1 == 'Papel':
                print('{}{} vence {}. Você venceu!{}'.format(cor['vd'], jg1, cpu, cor['0']))
                
        if cpu == 'Papel':
            if jg1 == 'Pedra':
                print('{}{} vence {}. Você perdeu!{}'.format(cor['vm'], cpu, jg1, cor['0']))
            elif jg1 == 'Tesoura':
                print('{}{} vence {}. Você venceu!{}'.format(cor['vd'], jg1, cpu, cor['0']))
                
        if cpu == 'Tesoura':
            if jg1 == 'Papel':
                print('{}{} vence {}. Você perdeu!{}'.format(cor['vm'], cpu, jg1, cor['0']))
            elif jg1 == 'Pedra':
                print('{}{} vence {}. Você venceu!{}'.format(cor['vd'], jg1, cpu, cor['0']))  

"""
# Solução do professor:
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
"""
