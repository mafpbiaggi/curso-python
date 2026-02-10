'''
Desafio 107: https://youtu.be/s3r8_Aug4y8?t=1618
Correção: https://youtu.be/y8pI8YBphQI

'''
sub = 'Exercitando Módulos em Python'

'''
Enunciado:
Crie um módulo chamado moeda.py que tenha funções incorporadas:
  - aumentar()
  - diminuir()
  - dobro()
  - metade()

Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda

# Main
print('=' * 60)
print(f'{"Desafio 107":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

n = float(input('Digite um preço: R$ '))

print(f'O valor 5 aumentado em 15% = {moeda.aumentar(n, 15)}')
print(f'O valor 5 diminuído em 25% = {moeda.diminuir(n, 25)}')
print(f'O dobro de 5 é {moeda.dobro(n)}')
print(f'A metade de 5 é {moeda.metade(n)}')

'''
# Solução do Professor:

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
'''
