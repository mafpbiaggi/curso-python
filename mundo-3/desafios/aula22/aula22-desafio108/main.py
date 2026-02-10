'''
Desafio 108: https://youtu.be/s3r8_Aug4y8?t=1728
Correção: 

'''
sub = 'Formatando Moedas em Python'

'''
Enunciado:
Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores como um valor monetário formatado.
'''
import moeda

# Main
print('=' * 60)
print(f'{"Desafio 108":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

num = float(input('Digite um número: R$ '))
print(f'\nA metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.')
print(f'O preço aumentado em 10% é {moeda.moeda(moeda.aumentar(num, 10))}.')
print(f'O preço diminuído em 37% é {moeda.moeda(moeda.diminuir(num, 37))}.')
