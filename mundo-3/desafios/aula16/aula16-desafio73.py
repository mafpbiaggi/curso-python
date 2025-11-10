'''
Desafio 73: https://youtu.be/0LB3FSfjvao?t=2696
Correção: https://youtu.be/RexybLcGewA

Enunciado:'''
sub = ' Tuplas com Times de Futebol'

'''Crie uma tupla preenchida com os 20 primeiros números colocados da Tabela do Campeonato Brasileiro de Futebos,
na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) os último 4 colocados.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da 'Chapecoense'.
'''
t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 73 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol',
        'Bahia', 'Botafogo', 'Fluminense', 'São Paulo',
        'Atlético-MG', 'Vasco da Gama', 'Bragantino', 'Ceará SC',
        'Corinthians', 'Grêmio', 'Internacional', 'EC Vitória',
        'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')

print(f'\nOs 5 primeiro colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}') # Corrigido
print(f'Os times em ordem alfabética são: {sorted(times)}')

# No ano que estou fazendo o exercício a Chape não está na Série A, então fiz uma condição.
if 'Chapecoense' not in times:
    print(f'A Chapecoense não está na Série A neste ano.')
else:
    print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição.')

"""
# Solução do professor:

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol',
        'Bahia', 'Botafogo', 'Fluminense', 'São Paulo',
        'Atlético-MG', 'Vasco da Gama', 'Bragantino', 'Ceará SC',
        'Corinthians', 'Grêmio', 'Internacional', 'EC Vitória',
        'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
"""
