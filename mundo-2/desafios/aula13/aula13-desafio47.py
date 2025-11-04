'''
Desafio 47: https://youtu.be/cL4YDtFnCt4?t=1664
Correção: https://youtu.be/Qws8-E-YrlY

Enunciado:
Crie um programa que mostre na tela todos os números pares que estão no interfavo entre 1 e 50.
'''

print('====== Desafio 47 ======\n')

print('Os números pares entre 1 e 50 são: ')
for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end='')
print('\n')

"""
# Solução do professor: Ele acabou alterando a lógica no laço, embora ele tenha colocado no enunciado que
# o contador deveria partir do 1. Essa solução faz menor repetições de laço, isso alivia processamento.

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
"""
