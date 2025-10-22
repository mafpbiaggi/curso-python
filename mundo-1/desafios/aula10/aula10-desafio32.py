# Desafio 32: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1794
# Correção:

# Enunciado:
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# O que é um ano bissexto:
# - Multiplos de 400
# - Múltiplos de 4, Multiplos de 100, mas não múltiplo de 400
print('====== Desafio 32 ======')

ano = int(input('Digite um ano (com 4 dígitos = 2025): '))

if ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print('O ano {} é bissexto'.format(ano))
    else:
        print('O ano {} não é bissexto.'. format(ano))
