'''
Desafio 101: https://youtu.be/etjJ_4Eqrk8?t=2400
Correção: https://www.youtube.com/watch?v=czDcimdc3GU&t=5s

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

def voto(a_nasc):
    from datetime import date

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

'''
# Solução do Professor:

def voto(ano):
    from datetime import date # Escopo de importação. Economia de memória
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

        
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
'''
