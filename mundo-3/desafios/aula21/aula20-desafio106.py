'''
Desafio 106: https://youtu.be/etjJ_4Eqrk8?t=2825
Correção: 

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
