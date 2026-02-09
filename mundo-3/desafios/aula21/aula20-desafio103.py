'''
Desafio 103: https://youtu.be/etjJ_4Eqrk8?t=2574
Correção: https://youtu.be/FbOvilKfHMI

'''
sub = 'Ficha do jogador'

'''
Enunciado:
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.

Exemplo:

    Nome do jogador: <vazio>
    Número de gols: <vazio>

    >>> O jogador <desconhecido> fez 0 gol(s) no campeonato.
'''

def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    
    if g.isnumeric() == False:
        g = 0

    return print(f'\nO jogador {n} fez {g} gol(s) no campeonato.')


# Main
print('=' * 60)
print(f'{"Desafio 103":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

nome = str(input('Digite o nome do jogador: ')).strip()
gols = input('Digite o número de gols: ')

ficha(nome, gols)
print('=' * 60)

'''
# Solução do Professor:

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
'''
