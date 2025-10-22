# Desafio 30: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1740
# Correção:

# Enunciado:
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('====== Desafio 30 ======')

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))
    