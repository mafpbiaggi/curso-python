'''
Desafio 53: https://youtu.be/cL4YDtFnCt4?t=1847
Correção: https://youtu.be/5VBWe6BXzRo

Enunciado:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços e acentos.

Ex: apos a sopa
    a sacada da casa
    a torre da derrota
    o lobo ama o bolo
    anotaram a data da maratona
'''
print('====== Desafio 53 ======')
print('É palíndromo?\n')

f = str(input('Digite uma frase: ')).strip().lower()
ft = f.replace(' ', '')

f_rev = ''
for i in range(len(ft)-1, -1, -1):
    f_rev = f_rev + ft[i]

if ft == f_rev:
    print('A frase "{}" é um palíndromo.'.format(f))
else:
    print('A frase "{}" não é um palíndromo.'.format(f))

"""
# Solução do professor:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' # É possível remover o for e substituir por inverso = junto[::-1]
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digita NÃO É um palíndromo!')
"""
