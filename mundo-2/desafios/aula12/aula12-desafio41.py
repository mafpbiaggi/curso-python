"""
Desafio 41: https://youtu.be/j9bYDjaAYzw?t=1321
Correção:

Enunciado:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostra sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date
print('====== Desafio 41 ======')

ano = int(input('Digite o ano de nascimento do atleta: '))
diff = date.today().year - ano

if diff <= 9:
    print('Categoria: MIRIM')
elif diff > 9 and diff <= 14:
    print('Categoria: INFANTIL')
elif diff > 14 and diff <= 19:
    print('Categoria: JUNIOR')
elif diff > 19 and diff <= 20:
    print('Categoria: SÊNIOR')
elif diff > 20:
    print('Categoria: MASTER')
