# Desafio 18: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1719
# Correção: https://youtu.be/9GvsphwW26k?si=c2kFiKwhZ8nJmqog
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
print('====== Desafio 18 ======')

n = float(input('Digite um ângulo: °'))
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))

print('O ângulo digitado foi {}. Portanto, seno = {:.2f}, cosseno = {:.2f}, tangente = {:.2f}'.format(n, seno, cosseno, tangente))