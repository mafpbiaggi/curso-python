'''
Desafio 104: https://youtu.be/etjJ_4Eqrk8?t=2631
Correção: 

'''
sub = 'Validando entrada de dados em Python'

'''
Enunciado:
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Enquanto um valor inteiro não for inserido, o programa continua pedindo um valor inteiro.

Ex: n = leiaInt('Digite um n' )
'''

def leiaInt(msg):
    valor = input(msg)
    
    print()
    while valor.isnumeric() == False:
        valor = input('Valor inválido. Digite um valor inteiro: ')
    
    return int(valor)
        

# Main
print('=' * 60)
print(f'{"Desafio 104":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

n = leiaInt('Digite um valor para "n": ')
print(f'\nO valor digitado foi: {n} do tipo {type(n)}.')
print('=' * 60)
