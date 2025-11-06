'''
Desafio 66: https://youtu.be/1OFp_-R2B2A?t=1725
Correção:

Enunciado: Vários números com flag.
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando
o flag.
'''

print('======== Desafio 66 =======')
print('= Vários números com flag =\n')

cont = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro [999 para sair]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('\nFim da execução ---- Resultado:')
print(f'Quantidade de números cadastrados: {cont}.')
print(f'A soma desses valores é {soma}.')
