# Desafio 6: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1903
# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('====== Desafio 6 ======\n')

n = int(input('Digite um número inteiro: '))

d = n * 2
t = n * 3
rq = n ** (1/2)

print('O número digitado foi {}, portanto:\nO dobro é {}.\nO triplo é {}. A raíz quadrada é {:.2f}.'.format(n, d, t, rq))