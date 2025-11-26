'''
Desafio: https://youtu.be/ZWj8o692qGY?t=2372
Correção: https://youtu.be/ETnExBCFeps

Enunciado:'''
sub = ' Unindo Dicionários e Listas '
'''
Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 94 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

pessoa = {}
pessoas = []
tot_idade = 0

while True:
    pessoa['nome'] = str(input('\nDigite o nome: ')).strip()

    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]:\033[m ')).strip().upper()
        if pessoa['sexo'] in 'MF' and pessoa['sexo'] != '':
            break
        print('\033[33mOpção inválida.', end=' ')
    pessoa['idade'] = int(input('Digite a idade: '))
    tot_idade += pessoa['idade'] 
    
    pessoas.append(pessoa.copy())

    while True:
        resp = str(input('Continuar cadastrando? [S/N]\033[m ')).strip().upper()
        if resp in 'SN' and resp != '':
            break
        print('\033[33mOpção inválida.', end=' ')

    if resp in 'N':
        break

print()
print('=' * 52)
print(f'{"Resultado":^52}')
print('-' * 52)
print(f'O total de pessoas cadastradas foi: {len(pessoas)}')

m_idade = tot_idade / len(pessoas)
print(f'A média de idade do grupo é: {m_idade:.2f} anos')

print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')

print('\nLista com todas as pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > m_idade:
        print(f'  -- Nome => {p["nome"]}, Sexo => {p["sexo"]}, Idade => {p["idade"]}')



'''
# Solução do professor:

pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'S':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')
'''
