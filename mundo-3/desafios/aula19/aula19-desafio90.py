'''
Desafio: https://youtu.be/ZWj8o692qGY?t=1836
Correção: https://youtu.be/HipQYUk4koA

Enunciado:'''
sub = ' Dicionário em Python '
'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.

Situação: Média >= 7 -> Aprovado.
          Média < 7  -> Reprovado.

Saída esperada: Nome é igual a {nome}
                Média é igual a {média}
                Situação é igual a {situação}
'''
t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 90 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

dados = {}
dados['nome'] = str(input('\nDigite o nome: ')).strip()
dados['media'] = float(input('Digite a média: '))

if dados['media'] < 7:
    dados['sitaucao'] = 'Reprovado'
else:
    dados['situacao'] = 'Aprovado'

print()
for k, v in dados.items():
    print(f'{k} é igual a {v}')

'''
# Solução do professor

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
'''
