'''
Desafio 112: https://youtu.be/s3r8_Aug4y8?t=2054
Correção: 

'''
sub = ''

'''
Enunciado:
Dentro do pacote utilizadadesCeV que criamos no desafio 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função
input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

O programa deve aceitar números com vírgula também, além de números com pontos dividindo
as casas decimais.
'''

from utilidadesCev import moeda, dado

# Main
print('=' * 60)
print(f'{"Desafio 112":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

num = dado.leiaDinheiro('Digite um preço: ')
moeda.resumo(num, 87, 22)
