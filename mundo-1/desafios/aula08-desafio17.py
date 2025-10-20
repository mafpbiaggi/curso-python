# Desafio 17: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1673
# Correção: https://youtu.be/vmPW9iWsYkY?si=scHwP_fcZ1ZNYzES

# Enunciado:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math
print('====== Desafio 17 =======')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print('C.Oposto: {}, C. Adjacente: {}. O valor da hipotenusa é {:.2f}'.format(co, ca, math.hypot(co, ca)))

'''Uso da maneira tradicional:
   hi = (co ** 2 + ca ** 2) ** (1/2)
   É possível importar também somente a função hypot() => from math import hypot'''