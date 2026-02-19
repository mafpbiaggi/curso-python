'''
Desafio 114: https://youtu.be/xz2B3bfNjEk?t=1781
Correção: https://youtu.be/8jAykqxIeqw
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

'''
# Solução do professor:

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')
'''
