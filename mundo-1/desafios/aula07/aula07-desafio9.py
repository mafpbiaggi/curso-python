# Desafio 9: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1960
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Cabeçalho
print('====== Desafio 9 =======\n')

# Recebe valor inteiro
n = int(input('Digite um número inteiro: '))

n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10

print('\nResultado:')
print('{} x  1 = {}'.format(n, n1))
print('{} x  2 = {}'.format(n, n2))
print('{} x  3 = {}'.format(n, n3))
print('{} x  4 = {}'.format(n, n4))
print('{} x  5 = {}'.format(n, n5))
print('{} x  6 = {}'.format(n, n6))
print('{} x  7 = {}'.format(n, n7))
print('{} x  8 = {}'.format(n, n8))
print('{} x  9 = {}'.format(n, n9))
print('{} x 10 = {}'.format(n, n10))

# Solução proposta em aula, sem uso de variáveis auxiliares

#n = int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#print('{} x {:2} = {}'.format(n, 1, n*1))
#print('{} x {:2} = {}'.format(n, 2, n*2))
#print('{} x {:2} = {}'.format(n, 3, n*3))
#print('{} x {:2} = {}'.format(n, 4, n*4))
#print('{} x {:2} = {}'.format(n, 5, n*5))
#print('{} x {:2} = {}'.format(n, 6, n*6))
#print('{} x {:2} = {}'.format(n, 7, n*7))
#print('{} x {:2} = {}'.format(n, 8, n*8))
#print('{} x {:2} = {}'.format(n, 9, n*9))
#print('{} x {:2} = {}'.format(n, 10, n*10))
#print('-' * 12)

# {:2} significa que o número inteiro ocupará 2 espaços.
# '-' * 12 = Replica os 12 vezes.