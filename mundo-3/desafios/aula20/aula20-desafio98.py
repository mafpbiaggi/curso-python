'''
Desafio 98: https://youtu.be/ezfr9d7wd_k?t=2571
Correção: https://youtu.be/DCBlt_z2UOE

'''
sub = 'Função de contador'

'''
Enunciado:
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo.
Por fim, realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Um contagem personalizada.
'''

from time import sleep

def titulo(t, s):
    print('=' * 60)
    print(f'{t:^60}')
    print('-' * 60)
    print(f'{s:^60}')
    print('-' * 60)

def contador(i, f, p):
    print(f'\nContador de {i} à {f}, passo {p}.')

    if i < f:
        f += 1
    else:
        f -= 1
        if p * -1 < 0:
            p *= -1

    for n in range(i, f, p):
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('Fim.')
    print('-' * 60)


titulo('Desafio 98', sub)

contador(0, 10, 1)
contador(10, 0, -2)

print('\nPersonalizando contador ...')
inicio = int(input(('\n   Digite o valor inicial: ')))
fim = int(input('   Digite o valor final: '))
passo = int(input('   Digite o passo: '))

if inicio != fim:
    if passo == 0:
        passo = 1
        print(f'   \033[33mValor (0) digitado para o passo. Valor padrão (1) aplicado.\033[m')
    contador(inicio, fim, passo)
else:
    print('\nO valor inicial e o final são iguais. Saindo ...')

'''
# Solução do professor:

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print('f{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
'''
