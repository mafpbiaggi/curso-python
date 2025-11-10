'''
Desafio 76: https://youtu.be/0LB3FSfjvao?t=2926
Correção:

Enunciado:'''
sub = ' Lista de Preços '

'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivo preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

Obs: listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)
'''

t_sub = int((52 - len(sub)) / 2)
print('=' * 20 + ' Desafio 76 ' + '=' * 20)
print('-' * t_sub + sub + '-' * t_sub + '\n')

tupla = ('Leite', 3.50, 'Refrigerante', 7.00, 'Chocolate', 4.99, 'Pão de Forma', 7.60, 'Bolacha', 2.69, 'Veja Multiuso', 5.80, 'Pneu', 480.76)

print('=' * 50)
print('{:^50}'.format('LISTA DE PREÇOS'))
print('-' * 50)

for item in range(0,len(tupla),2):
    print(f'{tupla[item]}'+'.'*(40-len(tupla[item]))+f'R$ {tupla[item+1]:7.2f}')

print('=' * 50)
