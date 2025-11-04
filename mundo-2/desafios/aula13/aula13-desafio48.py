'''
Desafio 48: https://youtu.be/cL4YDtFnCt4?t=1677
Correção:

Enunciado:
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''

print('====== Desafio 48 ======')

s = 0
for n in range(1, 500):
    if n % 2 != 0 and n % 3 == 0:
        s += n
print('A soma dos números ímpares, divisíveis por 3 entre 1 500 é: {}.'.format(s))
