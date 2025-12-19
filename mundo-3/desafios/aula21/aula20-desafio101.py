'''
Desafio 101: https://youtu.be/etjJ_4Eqrk8?t=2400
Correção: 

'''
sub = 'Funções para votação'

'''
Enunciado:
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal (palavra) indicando
se uma pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições.

< 18 = Não vota
entre 18 e 65 = Voto obrigatório
> 65 = Voto opcional
'''

from datetime import date


def voto(a_nasc):
    a_atual = date.today().year
    idade = a_atual - a_nasc

    if idade < 18:
        return 'Não vota'
    elif idade >= 18 and idade < 65:
        return 'Voto obrigatório'
    else:
        return 'Voto opcional'


# Main
print('=' * 60)
print(f'{"Desafio 101":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

nasc = int(input('Digite o ano de nascimento: '))
print(f'>>> {voto(nasc)}.')
print('-' * 60)
