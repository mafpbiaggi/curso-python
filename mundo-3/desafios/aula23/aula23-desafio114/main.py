'''
Desafio 114: https://youtu.be/xz2B3bfNjEk?t=1781
Correção:
'''
sub = 'Site está acessível?'

'''
Enunciado:
Crie um código em Python que teste se o site Pudim (pudim.com.br) está acessível pelo computador
usado.

Os resultados devem ser positivos e negativos, ou seja, se estiver, apresenta mensagem que
está acessível, caso contrário, outra mensagem que não está acessível.
'''

print('=' * 60)
print(f'{"Desafio 114":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

import func
func.checkSite('https://pudim.com.br')
