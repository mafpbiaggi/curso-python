'''
Desafio 82: https://youtu.be/N1hTsbW50eM?t=2106
Correção: https://youtu.be/uk0gDFQEo_I

Enunciado:'''
sub = ' Dividindo valores em várias listas '
'''Crie um programa que vai ler vários números e colocar em uma lista.
Perguntando se quer continuar.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 82 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

lista = []
l_par = []
l_impar = []

while True:
    lista.append(int(input('\nDigite um número: ')))

    while True:
        resp = str(input('Quer continuar? [S/N]\033[m ')).strip()
        if resp in 'SsNn' and resp != '':
            break
        print('\033[33mOpção inválida.', end=' ')

    if resp in 'Nn':
        break

for n in lista:
    if n % 2 == 0:
        l_par.append(n)
    else:
        l_impar.append(n)

print(f'\nLista inicial: {lista}')
print(f'Lista com números pares: {l_par}')
print(f'Lista com números ímpares: {l_impar}')

'''
# Solução do professor:

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
'''
