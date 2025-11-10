'''
Desafio 77: https://youtu.be/0LB3FSfjvao?t=2997
Correção:

Enunciado:'''
sub = ' Contando Vogais em Tupla '

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 77 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

tupla = ('marco', 'alyne', 'ederli', 'igreja', 'instrumento', 'musical', 'teclado',
         'computador', 'mesa', 'mouse', 'cadeira', 'amarelo', 'lei', 'caderno',
         'ensino', 'aprendizado', 'dedicado', 'tempo', 'lavagem', 'roupa')

for p in tupla:
    print(f'\nNa palavra "{p}", temos as vogais: ', end='')
    for i in range(len(p)):
        if 'a' in p[i]:
            print(f'{p[i]}', end=' ')
        if 'e' in p[i]:
            print(f'{p[i]}', end=' ')
        if 'i' in p[i]:
            print(f'{p[i]}', end=' ')
        if 'o' in p[i]:
            print(f'{p[i]}', end=' ')
        if 'u' in p[i]:
            print(f'{p[i]}', end=' ')
print()
