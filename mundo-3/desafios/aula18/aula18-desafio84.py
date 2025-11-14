'''
Desafio 84: https://youtu.be/YV_JQmZNFsk?t=1450
Correção: https://youtu.be/zPtvuLiEdKk

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

'''
# Solução do professor:
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
'''
