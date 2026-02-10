'''
Desafio 107: https://youtu.be/s3r8_Aug4y8?t=1618
Correção: 

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

print(f'O valor 5 aumentado em 15% = {moeda.aumentar(5, 15)}')
print(f'O valor 5 diminuído em 25% = {moeda.diminuir(5, 25)}')
print(f'O dobro de 5 é {moeda.dobro(5)}')
print(f'A metade de 5 é {moeda.metade(5)}')
