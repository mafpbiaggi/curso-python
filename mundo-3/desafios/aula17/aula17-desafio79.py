'''
Desafio 79: https://youtu.be/N1hTsbW50eM?t=1795
Correção:

Enunciado:'''
sub = ' Valores únicos em uma lista '

'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
O programa deve perguntar se o usuário quer continuar cadastrando. Caso o número já exista lá dentro,
ele não será adicionado e um alerta será exibido para o usuário. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 79 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)
lista = []

while True:    
    n = int(input('\nDigite um valor: '))
    
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso ...')

        while True:
            resp = str(input('Você quer continuar? [s/n]:\033[m ')).strip()
            if resp in 'SsNn' and resp != '':
                break
            print('\033[33mOpção inválida.', end=' ')
       
        if resp in 'Nn':
            break

    else:   
        print('Número não adicionado. Já está na lista ...')

lista.sort()
print('\n' + '-' * 52)
print(f'A lista de números digitados é {lista}.')
