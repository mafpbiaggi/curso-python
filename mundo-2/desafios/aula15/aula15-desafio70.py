"""
Desafio 70: https://youtu.be/1OFp_-R2B2A?t=2065
Correção:

Enunciado:"""
sub = ' Estatísticas em Produtos '
"""
Crie um programa que leia um nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000,00.
c) Que é o nome do produto mais barato.
"""

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 70 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

c_prod = 0
tot_compr = 0
c_m_mil = 0
c_m_barato = 0

while True:
    n_produto = str(input('\nDigite o nome do produto: ')).strip()
    p_produto = float(input('Digite o preço do produto: R$ '))
    if c_prod == 0:
        n_m_barato = n_produto
        c_m_barato = p_produto
    else:
        if p_produto < c_m_barato:
            n_m_barato = n_produto
            c_m_barato = p_produto

    if p_produto > 1000:
        c_m_mil += 1

    c_prod += 1
    tot_compr += p_produto

    prox = str(input('Você quer cadastrar mais produtos? [s/n]: ')).strip()
    while prox not in 'SsNn':
        prox = str(input('\033[33mOpção inválida. Digite novamente [s/n]:\033[m '))
    if prox in 'Nn':
        break

print(f'\nEncerrando compra -----\n{c_prod} produtos cadastrados.')
print(f'O valor total da compra é R$ {tot_compr:.2f}')
print(f'Quantidade de produtos com valor maior do que R$ 1000,00: {c_m_mil}.')
print(f'O produto mais barato é "{n_m_barato}", custando R$ {c_m_barato:.2f}.')
