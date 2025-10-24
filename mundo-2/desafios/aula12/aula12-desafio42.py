"""
Desafio 42: https://youtu.be/j9bYDjaAYzw?t=1358
Correção:

Enunciado:
Refaça o desafio 35 (dos triângulos), acrescentando o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

print('====== Desafio 42 ======')

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da secunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

cor = {'0':'\033[m', # Limpa formatação
       'vd':'\033[32m', # Cor: verde
       'vm':'\033[31m', # Cor: vermelho
       'b':'\033[1m'} # Estilo: negrito

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    
    # Define qual o tipo do triângulo
    if r1 == r2 and r2 == r3:
        tipo = 'equilátero'
    elif r1 == r2 or r2 == r3 or r1 == r3:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'

    print('{}As retas {}, {} e {} podem formar um triângulo {}.{}'.format(cor['vd'], r1, r2, r3, tipo, cor['0']))
else:
    print('{}As retas {}, {} e {} não podem formar um triângulo.{}'.format(cor['vm'], r1, r2, r3, cor['0']))
