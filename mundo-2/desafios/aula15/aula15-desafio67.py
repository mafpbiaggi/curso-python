'''
Desafio 67: https://youtu.be/1OFp_-R2B2A?t=1798
Correção:

Enunciado: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
from time import sleep
print('=' * 21 + ' Desafio 67 ' + '=' * 21)
print('-' * 20 + ' Tabuada v3.0 ' + '-' * 20)

while True:
    print('\nDigite um número para ver sua tabuada.')
    n = int(input('\033[33mPara sair do programa, digite um número negativo:\033[m '))
    print('-' * 54)

    if n < 0:
        break
    
    for cont in range(1, 11):
        print(f'{n:>22} x {cont:2} = {n*cont}')

    print('-' * 54)
    sleep(.70)
print('Fim da execução ---- Até mais.\n')
