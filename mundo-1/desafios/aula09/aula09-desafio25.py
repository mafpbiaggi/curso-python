# Desafio 25: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2575
# Correção: https://youtu.be/WHWGz2Dy1ZU?si=fU-UM6xgGsH9kTdl

# Enunciado:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('====== Desafio 25 ======')

nome = str(input('Digite seu nome completo: ')).strip()
print('Há "Silva" em {}? R: {}'.format(nome, 'silva' in nome.lower()))

'''Solução do professor:

  nome = str(input('Qual é o seu nome completo? ')).strip()
  print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
'''