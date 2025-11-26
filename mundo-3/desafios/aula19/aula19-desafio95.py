'''
Desafio: https://youtu.be/ZWj8o692qGY?t=2487
Correção: https://youtu.be/mw1So0r317Y

Enunciado:'''
sub = ' Aprimorando Dicionários '
'''
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.

Parecido com o desafio do boletim.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 95 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

jg = dict()
l_jg = list()
gols = list()
t_gols = 0

while True:
    jg['nome'] = str(input('\nDigite o nome do jogador: ')).strip()
    n_part = int(input(f'Digite a quantidade de partidas jogadas pelo {jg["nome"]}: '))

    print()
    for c in range(1, n_part+1):
        p_gols = int(input(f'   Quantos gols foram feitos na partida {c}: '))
        t_gols += p_gols
        gols.append(p_gols)

    jg['gols'] = gols[:]
    jg['total_gols'] = t_gols

    l_jg.append(jg.copy())
    
    gols.clear()
    t_gols = 0
    p_gols = 0

    print()
    while True:
        resp = str(input('Quer cadastrar outro jogador? [S/N]\033[m ')).strip().upper()
        if resp in 'SN':
            break
        print('\033[33mOpção inválida.', end=' ')

    if resp in 'N':
        break

print('\n' + '-' * 52)
print(f'{"Resumo":^52}')
print('-' * 52)
print(f'| {"#":<2} | {"Nome":<24} | {"Total de Gols":>16} |')
print('-' * 52)

for c, j in enumerate(l_jg):
    print(f'| {c:<2} | {j["nome"]:<24} | {j["total_gols"]:>16} |')
print('-' * 52)
print()

while True:
    r = int(input('Mostrar os gols de qual jogador? (999 para sair):\033[m '))
    if r == 999:
        print()
        break
    if r > len(l_jg)-1:
        print('\033[33mJogador inexistente.', end=' ')
    else:
        print()
        print('-' * 52)
        print(f'O jogador {l_jg[r]["nome"]} fez:\n')
        
        for i, j in enumerate(l_jg[r]["gols"]):
            print(f'    => {j} gol(s) na partida {i+1}')
        print('-' * 52)
        print()

print('-' * 52)
print(f'{"Finalizado":^52}')
print('-' * 52)

'''
# Solução do professor:

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}?' )))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True: 
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responsa apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jhogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca["nome"]]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez tantos {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
'''
