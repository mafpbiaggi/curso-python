# Desafio 5: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1856
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('====== Desafio 5 ======\n')
n = int(input('Digite um número inteiro: '))

a = n - 1
s = n + 1

print('O número digitado foi {}, portanto seu antecessor é {} e seu sucessor é {}'.format(n, a, s))