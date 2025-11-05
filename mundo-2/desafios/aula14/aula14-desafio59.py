'''
Desafio 59: https://youtu.be/LH6OIn2lBaI?t=1793
Correção: 

Enunciado:
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair

Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('====== Desafio 59 ======\n')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

menu = 0
while menu != 5:
    print('\n===== Menu de Operações =====')
    print('[ 1 ] -> Somar\n[ 2 ] -> Multiplicar\n[ 3 ] -> Maior\n[ 4 ] -> Novos Números\n[ 5 ] -> Sair')
    menu = int(input('Opção: '))
    
    if menu == 1:
        print('\nSoma -> {} + {} = {}.'.format(n1, n2, n1 + n2))

    if menu == 2:
        print('\nMultiplicação -> {} x {} = {}.'.format(n1, n2, n1 * n2))

    if menu == 3:
        maior = n1

        if n2 > n1:
            maior = n2
        print('\nO maior valor é {}.'.format(maior))

    if menu == 4:
        n1 = int(input('\nDigite um novo valor para o primeiro: '))
        n2 = int(input('Digite um novo valor para o segundo: '))
print('\nEncerrando ...')
