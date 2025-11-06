"""
Desafio 69: https://youtu.be/1OFp_-R2B2A?t=1935
Correção: https://youtu.be/4Ca6iRJo3M0

Enunciado:"""
sub =' Análise de dados - Grupo '

""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário que ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
"""

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 69 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

c_cadast = 0
c_homem = 0
c_idade = 0
c_m_menor = 0

print('Iniciando cadastro ...')
while True:
    idade = int(input('\nDigite a idade: '))
    if idade >= 18:
        c_idade += 1

    sexo = str(input('Digite o sexo [m/f] :')).strip()
    while sexo not in 'MmFf':
        sexo = str(input('\033[33mValor inválido. Digite novamente o sexo [m/f]:\033[m ')).strip()
    
    if sexo in 'Mm':
        c_homem += 1
    else:
        if idade < 20:
            c_m_menor += 1

    c_cadast += 1

    prox = str(input('Você quer continuar cadastrando? [s/n]: ')).strip()
    while prox not in 'SsNn':
        prox = str(input('\033[33mValor inválido. Digite novamente sua resposta [s/n]:\033[m '))
    if prox in 'Nn':
        break

print(f'\nEncerrando cadastro.\n{c_cadast} pessoas cadastradas.')
print(f'O número de pessoas com mais de 18 anos é {c_idade}')
print(f'A quantidade de homens cadastrados é {c_homem}.')
print(f'A quantidade de mulheres menores de 20 anos é {c_m_menor}')

"""
# Solução do professor:

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S?N] ')).strip().upper()[0]

    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cdastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
"""
