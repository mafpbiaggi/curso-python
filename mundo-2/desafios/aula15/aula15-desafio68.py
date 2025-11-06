'''
Desafio 68: https://youtu.be/1OFp_-R2B2A?t=1851
Correção: https://youtu.be/EIzgKCCDdc0

Enunciado: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.
'''

from random import randint
from time import sleep
print('=' * 22 + ' Desafio 68 ' + '=' * 22)
print('-' * 18 + ' Jogo: Par ou Ímpar ' + '-' * 18)

rodadas = 0
while True:
    p_i = str(input('\nVocê escolhe Par [P] ou Ímpar [I]? ')).strip()
    
    while p_i not in 'PpIi':
        p_i = str(input('\033[33mNão tem essa opção, escolha P ou I. Qual você escolhe?\033[m ')).strip()

    cpu = randint(1,50)
    jg1 = int(input('Ok, agora escolha um número: '))

    print('\nEntão, vamos lá ...')
    sleep(0.5)
    for i in range(1, 4):
        print(f'{i}... ', end='', flush=True)
        sleep(1)

    res = cpu + jg1
    if res % 2 == 0:
        res_ext = 'Par' 
    else:
        res_ext = 'Ímpar'

    print(f'=> CPU ({cpu}) + JG1 ({jg1}) = {res} .... \033[1m{res_ext}\033[m')

    if p_i in 'Pp' and res_ext == 'Par':
        print('\n\033[32mVocê venceu! vamos de novo ...\033[m')
        rodadas += 1
    elif p_i in 'Ii' and res_ext == 'Ímpar':
        print('\n\033[32mVocê venceu! vamos de novo ...\033[m')
        rodadas += 1
    else:
        break

print('\n\033[31mVocê perdeu!\033[m')
print(f'Você venceu {rodadas} partidas consecutivas.')

"""
# Solução do professor:

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] # Não utilizei esse método [0], porque não quero que o jogador digite Par, apenas o P mesmo.
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {v} vezes.')
"""
