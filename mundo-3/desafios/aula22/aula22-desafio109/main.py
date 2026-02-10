'''
Desafio 109: https://youtu.be/s3r8_Aug4y8?t=1789
Correção: https://youtu.be/Y0zNYTHoGhQ

'''
sub = ''

'''
Enunciado:
Modifique as funções que foram criadas no desafio 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser,
ou não, formatado pela função moeda(), desenvolvida no desafio 108.
'''

import moeda

# Main
print('=' * 60)
print(f'{"Desafio 109":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

num = float(input('Digite um número: R$ '))
print(f'\nA metade de {moeda.moeda(num)} {moeda.metade(num, True)}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, False)}.')
print(f'O preço aumentado em 41% é {moeda.aumentar(num, 41)}.')
print(f'O preço diminuído em 29% é {moeda.diminuir(num, 29, format=True)}.')

'''
# Solução do Professor:

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
'''
