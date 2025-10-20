# Desafio 27: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2635
# Correção:

# Enunciado:
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
#   Ex: Ana Maria de Souza
#   Primeiro = Ana
#   Último = Souza

print('====== Desafio 27 ======')

nome = str(input('Digite seu nome completo: '))
nome_div = nome.split()

print('Seu nome completo é: {}'. format(nome.title()))
print('Seu primeiro nome é {}'.format(nome_div[0]))
print('Seu último nome é {}'.format(nome_div[len(nome_div) - 1]))