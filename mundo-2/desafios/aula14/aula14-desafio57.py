'''
Desafio 57: https://youtu.be/LH6OIn2lBaI?t=1669
Correção: https://youtu.be/JGztEBLGj5E

Enunciado:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter o valor correto.
'''

print('====== Desafio 57 ======')
print('Validação de Sexo\n')

s = str(input('Digite qual o seu sexo [M/F]: ')).strip().upper()
while s not in 'MmFf':
    print('Opção inválida: "{}".'.format(s), end=' ')
    s = str(input('Digite novamente: ')).strip().upper()
print('Seu sexo é {}.'.format(s))

"""
# Solução do professor:

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # Coleta somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

"""
