'''
Desafio 81: https://youtu.be/N1hTsbW50eM?t=2008
Correção:

Enunciado:'''
sub = ' Extraindo dados da lista '
'''Crie um programa que vai ler vários números e colocar em uma lista.
Perguntando se o usuário quer continuar. Depois disso, mostre:

a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 81 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

lista = []
while True:
    lista.append(int(input('\nDigite um número: ')))
    
    while True:
        resp = str(input('Quer continuar? [S/N]\033[m ')).strip()
        if resp in 'SsNn' and resp != '':
            break
        print('\033[33mOpção inválida.', end=' ')
    
    if resp in 'Nn':
        break

print(f'\nA quantidade de números digitados cadastrados foi: {len(lista)}.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print(f'O número 5 não foi digitado e não está na lista.')
