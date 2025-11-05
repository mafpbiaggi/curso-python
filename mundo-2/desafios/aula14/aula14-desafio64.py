'''
Desafio 64: https://youtu.be/LH6OIn2lBaI?t=2047
Correção: https://youtu.be/mYlbttiLHM0

Enunciado:
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag - 999).
'''

print('====== Desafio 64 ======')
print('==== Conta e Soma =====\n')

n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número inteiro (999 para sair): '))
    if n != 999:
        s += n
        c += 1
       
print('\nVocê digitou {} números e a soma deles é {}.'.format(c, s))

'''
# Solução do professor:

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
'''
                  