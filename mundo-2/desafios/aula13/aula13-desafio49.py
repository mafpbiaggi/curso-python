'''
Desafio 49: https://youtu.be/cL4YDtFnCt4?t=1712
Correção: https://youtu.be/QtElJDa9ICM

Enunciado:
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for
'''
print('====== Desafio 49 ======\n')
n = int(input('Digite um número inteiro: '))

print('\nTabuada ...')
for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))

"""
# Solução do professor:
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
"""
