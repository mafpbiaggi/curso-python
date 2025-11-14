'''
Desafio 89: https://youtu.be/YV_JQmZNFsk?t=1982
Correção:

Enunciado:'''
sub = ' Boletim '
'''Crie um programa que leia nome e duas notas de vários alunos (Quer continuar?) e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
inidividualmente.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 85 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

bd = []
aluno = []
notas = []
media = 0

while True:
    aluno.append(str(input('\nDigite o nome do aluno: ')).strip())
    notas.append(float(input('Digite a N1: ')))
    notas.append(float(input('Digite a N2: ')))

    for n in notas:
        media += n
    
    notas.append(media/2)
    aluno.append(notas[:])
    bd.append(aluno[:])
    notas.clear()
    aluno.clear()
    media = 0

    while True:
        resp = str(input('Inserir outro aluno? [S/N]\033[m ')).strip()
        if resp in 'SsNn' and resp != '':
            break
        print('\033[33mOpção inválida.', end=' ')
    
    if resp in 'Nn':
        break

print('\n' + '-' * 52)
print(f'{"Resultado":^52}')
print('-' * 52)
print(f'| {"#":<2} | {"Nome":<24} | {"Média":>16} |')
print('-' * 52)

for c, item in enumerate(bd):
    print(f'| {c:<2} | {item[0]:<24} | {item[1][2]:>16.2f} |')
print('-' * 52)
print()

while True:
    r = int(input('Mostrar as notas de qual aluno? (999 para sair):\033[m '))
    if r == 999:
        print()
        break
    if r > len(bd)-1:
        print('\033[33mAluno inexistente.', end=' ')
    else:
        print()
        print('-' * 52)
        print(f'| {"#":<2} | {"Nome":<24} | {"N1":>6} | {"N2":>7} |')
        print('-' * 52)
        print(f'| {r:<2} | {bd[r][0]:<24} | {bd[r][1][0]:>6.2f} | {bd[r][1][1]:>7.2f} |')
        print('-' * 52)
        print()

print('-' * 52)
print(f'{"Finalizado":^52}')
