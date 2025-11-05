'''
Desafio 57: https://youtu.be/LH6OIn2lBaI?t=1669
Correção:

Enunciado:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter o valor correto.
'''

print('====== Desafio 57 ======')
print('Validação de Sexo\n')

s = str(input('Digite qual o seu sexo [M/F]: ')).strip().upper()
while s != 'M' and s != 'F':
    print('Opção inválida: "{}".'.format(s), end=' ')
    s = str(input('Digite novamente: ')).strip().upper()
print('Seu sexo é {}.'.format(s))
