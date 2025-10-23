# Desafio 35: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1866
# Correção: https://youtu.be/NZiNphKkxhg

# Enunciado:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem ou não
# formar um triângulo.

print('====== Desafio 35 ======')

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da secunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas {}, {}, {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('As retas {}, {}, {} não podem formar um triângulo.'.format(r1, r2, r3))
    
# Solução do professor:
'''
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acime PODEM FORMAR trinângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
'''
