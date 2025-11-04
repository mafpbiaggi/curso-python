'''
Desafio 54: https://youtu.be/cL4YDtFnCt4?t=1919
Correção:

Enunciado:
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade (21 anos) e quantas já são maiores.
'''
from datetime import date
print('====== Desafio 54 ======')
print('Verificação de Maioridade\n')

n = []
menores = []
maiores = []
a_atual = date.today().year
menor = 0
maior = 0

for i in range(0, 7):
    n.append(int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1))))

    if a_atual - n[i] < 21:
        menores.append(n[i])
        menor += 1

    else:
        maiores.append(n[i])
        maior += 1

print('\nResultado ...')
print('{} são menores de 21 anos e nasceram nos anos {}.'.format(menor, ', '.join(map(str, menores))))
print('{} são maiores de 21 anos e nasceram nos anos {}.'.format(maior, ', '.join(map(str, maiores))))
