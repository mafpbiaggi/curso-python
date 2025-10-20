# Desafio 22: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2447
# Correção:

# Enunciado:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#    O nome com todas as letras maiúsculas
#    O nome com todas as letras minúsculas
#    Quantas letras ao todo (sem considerar espaços)
#    Quantas letras tem o primeiro nome

print('====== Desafio 22 ======')

nome = str(input('Digite o seu nome completo: '))
p_nome = nome.split()

print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome ({}) tem {} letras.'.format(p_nome[0], len(p_nome[0])))