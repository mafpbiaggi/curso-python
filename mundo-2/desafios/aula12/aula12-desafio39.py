"""
Desafio 39: https://youtu.be/j9bYDjaAYzw?t=1212
Correção:

Enunciado:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falra ou que passou do prazo.
"""
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print('Você ainda tem {} anos para se alistar no serviço militar.'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar no serviço militar ainda este ano ({}).'.format(ano + 18))
elif idade > 18:
    print('Você se alistou, ou deveria ter se alistado há {} anos.'.format(idade - 18))
