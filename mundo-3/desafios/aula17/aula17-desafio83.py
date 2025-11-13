'''
Desafio 83: https://youtu.be/N1hTsbW50eM?t=2223
Correção: https://youtu.be/dvhP41Z7TLk

Enunciado:''' 
sub = ' Validador de Expressão '
'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 82 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub)

expr = str(input('\nDigite a expressão: '))
aux = []

for c in expr:
    if c == '{' or c == '[' or c == '(':
        aux.append(c)
    elif c == ')':
        if len(aux) > 0 and aux[-1] == '(':
            aux.pop()
        else:
            aux.append(c)
            break
    elif c == ']':
        if len(aux) > 0 and aux[-1] == '[':
            aux.pop()
        else:
            aux.append(c)
            break
    elif c == '}':
        if len(aux) > 0 and aux[-1] == '{':
            aux.pop()
        else:
            aux.append(c)
            break
if len(aux) == 0:
    print(True)
else:
    print(False)

'''
# Solução do professor: 
expr = str(input('Digite a expressão: '))
pilha = []

for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
'''
