# Desafio 33: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1819
# Correção:

# Enunciado:
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('====== Desafio 33 ======')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

men = n1
mai = n1

if n2 > mai:
    mai = n2

if n2 < men:
    men = n2

if n3 > mai:
    mai = n3

if n3 < men:
    men = n3

print('O menor número é {} e o maior número é {}.'.format(men, mai))
