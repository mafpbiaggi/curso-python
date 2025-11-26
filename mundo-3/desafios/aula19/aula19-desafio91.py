'''
Desafio: https://youtu.be/ZWj8o692qGY?t=1903
Correção: https://youtu.be/cwrqIztaAwk

Enunciado:'''
sub = ' Jogo de Dados em Python '
'''
Crie um programa onde 4 jogadores joguem um dado (6 lados) e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

Saída esperada:
    Valores sorteados:
        O jogador1 tirou X
        O jogador2 tirou X
        O jogador3 tirou X
        O jogador4 tirou X
    Ranking dos jogadores:
        1º lugar: jogadorY com x
        2º lugar: jogadorY com x
        3º lugar: jogadorY com x
        4º lugar: jogadorY com x
'''
from random import randint
from time import sleep
from operator import itemgetter

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 91 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

jgs = dict()
rkng = list()
print('\nRolando os dados ...\n')

for c in range(1, 5):
    key = f'Jogador {c}'
    val = randint(1, 6)
    jgs.update({key:val})
    print(f'O {key} tirou {val}')
    sleep(0.5)

print('\nRanking dos jogadores ...\n')
rkng = sorted(jgs.items(), key=itemgetter(1), reverse=True)
for r, v in enumerate(rkng):
    print(f'{r+1}º lugar: {v[0]} => dado: {v[1]}.')
    sleep(0.5)

# Observação, não consegui fazer esse exercício sem ver a correção.

'''
# Solução do professor:
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
'''