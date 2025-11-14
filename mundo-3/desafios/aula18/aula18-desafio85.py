'''
Desafio 85: https://youtu.be/YV_JQmZNFsk?t=1571
Correção:

Enunciado:'''
sub = ' Lista com pares e ímpares '

'''Crie um programa onde o usuário possa digitar sete valores numérico e cadatre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 85 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

l_num = [[],[]]

print()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número inteiro: '))
    
    if n % 2 == 0:
        l_num[0].append(n)
    else:
        l_num[1].append(n)

print('\n' + '-' * 52)
print(f'A lista completa é {l_num}')
l_num[0].sort()
l_num[1].sort()
print(f'A lista de números pares é {l_num[0]}')
print(f'A lista de números ímpares é {l_num[1]}')
