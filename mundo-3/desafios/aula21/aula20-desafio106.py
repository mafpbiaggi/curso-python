'''
Desafio 106: https://youtu.be/etjJ_4Eqrk8?t=2825
Correção: https://youtu.be/BMKYnZoxy88

'''
sub = 'Interactive helping system in Python'

'''
Enunciado:
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

Obs: Utilize cores.
'''

from pydoc import render_doc


def header():
    print('\033[34;46m')
    print('-' * 80)
    print(f'{sub:^80}')
    print('-' * 80 + '\033[m')


def intHelp(cmd):
    print('\033[30;42m')
    print('-' * 80)
    print(f'{"Acessando página do manual":^80}')
    print('-' * 80 + '\033[m')
    print('\033[32;40m')    
    print(f'{render_doc(cmd)}\033[m')


def endHelp():
    print('\033[37;43m')
    print('-' * 80)
    print(f'{"Saindo do sistema ... ":^80}')
    print('-' * 80 + '\033[m')


# Main
print('=' * 80)
print(f'{"Desafio 106":^80}')

while True:
    header()
    comando = str(input('\nFunção ou Lib > ')).strip()

    if comando not in 'fimFIM':
        intHelp(comando)
    else:
        endHelp()
        break

'''
# Solução do Professor:

from time import sleep
c = ('\33[m',       # 0 - sem cor
     '\33[0;30;41m' # 1 - vermelho
     '\33[0;30;42m' # 2 - verde
     '\33[0;30;43m' # 3 - amarelo
     '\33[0;30;44m' # 4 - azul
     '\33[0;30;45m' # 5 - roxo
     '\33[7;30m'    # 6 - branco
    );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(F'  msg')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
'''
