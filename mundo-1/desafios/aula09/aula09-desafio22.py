# Desafio 22: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2447
# Correção: https://youtu.be/EQQt-6QqXOs?si=kVyW2_hLUs_D74UL

# Enunciado:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#    O nome com todas as letras maiúsculas
#    O nome com todas as letras minúsculas
#    Quantas letras ao todo (sem considerar espaços)
#    Quantas letras tem o primeiro nome

print('====== Desafio 22 ======')

nome = str(input('Digite o seu nome completo: ')).strip()
p_nome = nome.split()

print('Analisando seu nome ...')
print('Em letras maiúsculas: {}.'.format(nome.upper()))
print('Em letras minúsculas: {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome ({}) tem {} letras.'.format(p_nome[0], len(p_nome[0])))


''' Solução do professor
nome = str(input('Digite o seu nome completo: ')).split() # Elimina os espaços antes e depois do nome.
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' '))) # Calcula os espaços presentes no meio dos nomes e subtrai do total de caracteres.
print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) # O primeiro espaço significa que a primeira palavra acabou, portanto, é o número de letras do primeiro nome.
'''