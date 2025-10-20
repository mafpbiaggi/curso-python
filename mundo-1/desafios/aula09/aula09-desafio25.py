# Desafio 25: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2575
# Correção:

# Enunciado:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('====== Desafio 25 ======')

nome = str(input('Digite seu nome completo: '))
print('Há "SILVA" em {}? R: {}'.format(nome, 'silva' in nome.lower()))


'''Solução com condicional (ainda não ensinado nas aulas)

if 'silva' in nome.lower():
    print('Seu nome é {} e SIM, há SILVA no seu nome.'.format(nome))
else:
    print('Seu nome é {} e NÃO há SILVA no seu nome'.format(nome))'''