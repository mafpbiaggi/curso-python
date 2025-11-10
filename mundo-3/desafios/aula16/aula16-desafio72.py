'''
Desafio 72: https://youtu.be/0LB3FSfjvao?t=2601
Correção:

Enunciado:'''
sub = ' Número por Extenso '

''''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por exteno, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Observação: Validação de input.
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 19 + ' Desafio 72 ' + '=' * 19)
print('-' * t_sub + sub + '-' * t_sub)

n_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('\nDigite um número entre 0 à 20: '))
while n < 0 or n > 20:
    n = int(input('\033[33mValor incorreto, digite novamente (entre 0 e 20):\033[m '))

print(f'O número digitado foi {n_extenso[n]}.')
