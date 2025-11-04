'''
Desafio 46: https://youtu.be/cL4YDtFnCt4?t=1596
Correção:

Enunciado:
Faça um programa que mostre na tela uma contegem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
print('====== Desafio 46 =======\n')

print('Contagem Regressiva ...')
for i in range(10, 0, -1):
    print('{} ...'.format(i))
    sleep(1)

print('Booooooom, Explosão de Fogos!!!')
