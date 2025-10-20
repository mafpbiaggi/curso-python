# Desafio 26: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2602
# Correção: https://youtu.be/23UOVEetNPY?si=r0-38iBMefpyMZUd

# Enunciado:
# Faça um programa que leia uma frase pelo teclado e mostre:
#    Quantas vezes aparece a letra "A".
#    Em que posição ela aparece a primeira vez.
#    Em que posição ela aparece a última vez.

print('===== Desafio 26 ======')

f = str(input('Digite uma frase: ')).strip()

print('\nAnalisando a frase ... "{}"'.format(f))
print ('A letra "a" aparece {} vezes na frase.'.format(f.lower().count('a')))
print('A primeira posição em que a letra aparece é: {}'.format(f.lower().find('a') + 1))
print('A última posição em que a letra aparece é: {}'. format(f.lower().rfind('a') + 1))

'''Sugestões do professor:

Para os números das posições ficarem legíveis para o usuário, adicionar 1 à posição.
Caso contrário, ele precisa saber que todo array começa com [0].'''