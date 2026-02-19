'''
Desafio 113: https://youtu.be/xz2B3bfNjEk?t=1641
Correção: https://youtu.be/KowQ_UIMuI8
'''
sub = 'Funções Aprofundadas em Python'

'''
Enunciado:
Reescreva a função leiaInt() que fizemos no desafio104, incluindo agora
a possibilidade de digitação de um número de tipo inválido.

Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

A exceção deve retornar um erro com algo:
ERRO: Por favor, digite um número inteiro válido (em vermelho).

Deve haver exceção de interrupção e, caso nenhum dos valores seja inserido,
o valor padrão deve ser 0.
'''
import func

print('=' * 60)
print(f'{"Desafio 113":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

num = func.leiaInt('\nDigite um número inteiro: ')
numf = func.leiaFloat('Digite um número real: ')
print(f'\nOs números informados foram {num} e {numf:.2f}')

'''
# Solução do professor:

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
'''
