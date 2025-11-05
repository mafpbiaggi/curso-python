'''
Desafio 59: https://youtu.be/LH6OIn2lBaI?t=1793
Correção: https://youtu.be/OBJL5vPj4-E

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
        print('\nO maior valor entre {} e {} é {}.'.format(n1, n2, maior))

    if menu == 4:
        n1 = int(input('\nDigite um novo valor para o primeiro: '))
        n2 = int(input('Digite um novo valor para o segundo: '))
print('\nEncerrando ...')



"""
# Solução do professor:

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os número novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando o programa.')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
"""
