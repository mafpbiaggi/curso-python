'''
Desafio 39: https://youtu.be/j9bYDjaAYzw?t=1212
Correção: https://youtu.be/ePwP4gU_waY

Enunciado:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falra ou que passou do prazo.
'''

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print('Você ainda tem {} anos para se alistar no serviço militar.'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar no serviço militar ainda este ano.')
elif idade > 18:
    print('Você se alistou, ou deveria ter se alistado há {} anos.'.format(idade - 18))

'''
# Solução do professor:
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano.'.format(ano))
'''
