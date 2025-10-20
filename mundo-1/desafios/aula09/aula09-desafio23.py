# Desafio 23: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2521
# Correção:

# Enunciado:
# Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos dígitos separados
#     Ex: Digite um número: 1834
#         Unidade: 4
#         Dezena: 3
#         Centena: 8
#         Milhar: 1

print('===== Desafio 23 ======')

# Solução com String
n = str(input('Digite um número de 0 à 9999: '))

print('O número digitado foi {}'.format(n))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'. format(n[0]))