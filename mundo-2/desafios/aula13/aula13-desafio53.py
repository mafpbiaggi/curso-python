'''
Desafio 53: https://youtu.be/cL4YDtFnCt4?t=1847
Correção:

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

f = str(input('Digite uma frase: ')).strip()
ft = f.replace(' ', '')

f_rev = ''
for i in range(len(ft)-1, -1, -1):
    f_rev = f_rev + ft[i]

if ft == f_rev:
    print('A frase "{}" é um palíndromo.'.format(f))
else:
    print('A frase "{}" não é um palíndromo.'.format(f))
