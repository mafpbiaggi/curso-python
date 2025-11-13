'''
Desafio 80: https://youtu.be/N1hTsbW50eM?t=1897
Correção: https://youtu.be/QDpwjBYRcVE

Enunciado:'''
sub = ' Lista ordenada sem repetições '
'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()), mostrando em qual posição ele foi inserido.

No final, mostre a lista ordenada na tela.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 80 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

lista = []
for i in range(1, 6):
    n = int(input(f'\nDigite o {i}º número: '))
    
    if i == 1 or n > lista[-1]:
        lista.append(n)
        print('Número inserido no final da lista.')
    else:
        j = 0
        while j < len(lista):
            if n < lista[j]:
                lista.insert(j, n)
                print(f'Número inserido na posição {j}.')
                break
            j += 1

print(f'\nOs números inseridos foram: {lista}')

'''
# Solução do professor:

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print('Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
'''
