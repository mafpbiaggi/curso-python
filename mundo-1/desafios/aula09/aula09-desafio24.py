# Desafio 24: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2553
# Correção:

# Enunciado:
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print('===== Desafio 24 ======')

cidade = str(input('Digite o nome de uma cidade: '))
filtra = cidade.split()

print('O nome da cidade é {}.'.format(cidade))
print('Ela começa com a palavra "santo"? R: {}'.format('santo' in filtra[0].lower()))