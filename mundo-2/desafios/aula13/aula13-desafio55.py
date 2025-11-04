'''
Desafio 55: https://youtu.be/cL4YDtFnCt4?t=1946
Correção:

Enunciado:
Faça um programa que leia o peso de cinco pessoas. No fina mostre qual foi o maior e o menor peso lidos.
'''

print('====== Desafio 55 ======')
print('Comparação de Peso\n')

menor = 0
maior = 0

for i in range(0, 5):
    p = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))
   
    if i == 0: # Primeira execução do laço
        menor = p
        maior = p
    else:
        if p < menor:
            menor = p
        elif p > maior:
            maior = p
    
print('\nResultado ...')
print('A pessoa mais pesada pesa {:.2f} Kg'.format(maior))
print('A pessoa mais leve pesa {:.2f} Kg'.format(menor))
