'''
Desafio 84: https://youtu.be/YV_JQmZNFsk?t=1450
Correção:

Enunciado:'''
sub = ' Lista composta e análise de dados '

'''Faça um programa que leia nome e peso de várias pessoas (Quer continuar?), guardando tudo em uma lista.
No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 84 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

pessoas = []
temp = []
p_pessadas = []
p_leves = []
tot_pess = 0
maior_peso = 0
menor_peso = 0

while True:
    temp.append(str(input('\nDigite o nome: ')).strip().title())
    temp.append(float(input('Digite o peso: ')))
    pessoas.append(temp[:])
    tot_pess += 1
    
    if maior_peso == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]
    
    temp.clear()
    
    while True:
        resp = str(input('Você quer continuar? [S/N]\033[m ')).strip()
        if resp in 'SsNn' and resp != '':
            break
        print('\033[33mValor inválido.', end=' ')
    
    if resp in 'Nn':
        break

print('\nAnalisando os dados ...')
print(f'O total de pessoas cadastradas é {tot_pess}.')
print(f'O maior peso cadastrado foi {maior_peso:.1f} Kg, das seguintes pessoas: ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'["{p[0]}"] ', end='')
print(f'\nO menor peso cadastrado foi {menor_peso:.1f} Kg, das seguintes pessoas: ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'["{p[0]}"] ' , end='')
print()
