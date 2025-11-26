'''
Desafio: https://youtu.be/ZWj8o692qGY?t=2037
Correção: https://youtu.be/Vsqemzdrj78

Enunciado:'''
sub = ' Cadastro de Trabalhador em Python '
'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

Obs: 
    Nâo guardar o ano de nascimento, apenas a idade.
    Considere 35 anos de contribuição para o cálculo da aposentadoria.

Saída esperada:
    Dicionário completo (Opcional).
    nome tem o valor Gustavo
    idade tem o valor 40
    ctps tem o valor 1234
    contratação tem o valor 1995
    salário tem o valor 1000.0
    aposentadoria tem o valor 52

'''
from datetime import date

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 92 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

trab = {}
ano_atual = date.today().year

trab['nome'] = str(input('\nDigite o nome: ')).strip()
ano_nasc = int(input('Digite o ano de nascimento: '))
trab['idade'] = ano_atual - ano_nasc
trab['ctps'] = int(input('Digite o número da CTPS (0 -> não possui):  '))

if trab['ctps'] > 0:
    trab['contratacao'] = int(input('\n   Digite o ano de contratação: '))
    trab['salario'] = float(input('   Digite o valor do salário: R$ '))
    trab['aposentadoria'] = trab['contratacao'] - ano_nasc + 35

print('\n' + '=' * 52)
print(f'{"Resultado":^52}')
print('-' * 52)

print(f'\nDicionário completo: {trab}')
for k, v in trab.items():
    print(f'{k} tem o valor {v}')

'''
# Solução do professor:

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasci = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(intpu('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}.')
'''
