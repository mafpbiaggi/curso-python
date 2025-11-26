'''
Desafio: https://youtu.be/ZWj8o692qGY?t=2217
Correção: https://youtu.be/5yKiud-YNaE

Enunciado:'''
sub = ' Cadastro de Jogador de Futebol '
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.

Saída esperada:
    Dicionário completo. Atenção, os gols são adicionados a uma lista.
    O campo nome tem o valor Joelson.
    O campo gols tem o valor [x,y,t,x,c]
    O campo total tem o valor w

    O jogador Joelson jogou N partidas
        => Na partida 0, fez X gols
        => Na partida 1, fez Y gols
        => Na partida 2, fez T gols
        [...]
'''

t_sub = int((60 - len(sub)) / 2)
print('=' * 24 + ' Desafio 93 ' + '=' * 24)
print('-' * t_sub + sub + '-' * t_sub)

jg = {}
gols = []
t_gols = 0

jg['nome'] = str(input('\nDigite o nome do jogador: ')).strip()
n_part = int(input(f'Digite a quantidade de partidas jogadas pelo {jg["nome"]}: '))

print()
for c in range(1, n_part+1):
    p_gols = int(input(f'   Quantos gols foram feitos na partida {c}: '))
    t_gols += p_gols
    gols.append(p_gols)

jg['gols'] = gols[:]
jg['total_gols'] = t_gols

print('\n' + '=' * 60)
print(f'{"Resultado da Análise":^60}')

print('-' * 60)
print(jg)

print('-' * 60)
for k, v in jg.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 60)
print(f'O jogador {jg["nome"]} jogou {n_part} partidas e fez:')
for i, j in enumerate(gols):
    print(f'    => {j} gol(s) na partida {i+1}')

'''
# Solução do professor:

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}?' )))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''
