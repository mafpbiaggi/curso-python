'''
Desafio 73: https://youtu.be/0LB3FSfjvao?t=2696
Correção:

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

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco da Gama', 'Bragantino', 'Ceará SC', 'Corinthians', 'Grêmio', 'Internacional', 'EC Vitória', 'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')

print(f'\nOs 5 primeiro colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[16:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')

if times.count('Chapecoense') == 0:
    print(f'A Chapecoense não está na Série A neste ano.')
else:
    print(f'O time da Chapecoense está na {times.index("Vasco da Gama")+1}ª posição.')
