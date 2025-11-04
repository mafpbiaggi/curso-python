'''
Desafio 47: https://youtu.be/cL4YDtFnCt4?t=1664
Correção:

Enunciado:
Crie um programa que mostre na tela todos os números pares que estão no interfavo entre 1 e 50.
'''
print('====== Desafio 47 ======\n')

print('Os números pares entre 1 e 50 são:')
for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end='')
print('\n')
