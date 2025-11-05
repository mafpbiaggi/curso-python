'''
Desafio 65: https://youtu.be/LH6OIn2lBaI?t=2079
Correção: https://youtu.be/QNPuPlPM--0

Enunciado:
Crie um programa que leia vários números inteiros pelo teclado. No final, da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
print('====== Desafio 65 ======')
print('=== Analisa Valores ===\n')

r = 's'
c = 0
s = 0
maior = 0
menor = 0

while r in 'Ss':
    n = int(input('Digite um número inteiro: '))
    s += n
    c += 1
    
    if c == 1:
        maior = n
        menor = n
    
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n
    
    r = str(input('Você quer continuar inserindo números? [s/n]: ')).strip()
    
    while r not in 'SsNn':
        r = str(input('Valor inválido. Digite novamente [s/n]: ')).strip()

print('\nResultado ...')
print('Você digitou {} valor(es) e ...'.format(c))
print('A média dos valores digitados é {}.'.format(s/c))
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
    
'''
# Solução do professor:
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(inpu('Digite um número: '))
    soma += núm
    quant += 1
    resp = str(input('Que continuar? [S/N]: ')).upper().strip()[0]
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''
