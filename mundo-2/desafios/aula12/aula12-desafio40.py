"""
Desafio: 40: https://youtu.be/j9bYDjaAYzw?t=1296
Correção: https://youtu.be/QuWDyUeoaJs?si=E-ZSFMocDffpa5OF

Enunciado:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

print('====== Desafio 40 ======\n')

cor = {'0':'\033[m',
       'vm':'\033[31m',
       'vd':'\033[32m',
       'am':'\033[33m',
       'b':'\033[1m'}

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print('\n{}Média: {:.2f} => REPROVADO.{}'.format(cor['vm'], m, cor['0']))
elif m >= 5.0 and m <= 6.9:
    print('\n{}Média: {:.2f} => RECUPERAÇÃO.{}'.format(cor['am'], m, cor['0']))
elif m >= 7.0:
    print('\n{}Média: {:.2f} => APROVADO'.format(cor['vd'], m, cor['0']))

'''
# Solução do professor:
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do alune é {:.1f}.'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O alune está em RECUPERAÇÃO.')
elif média < 5:
    print('O alune está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
'''
    