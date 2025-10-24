"""
Desafio 43: https://youtu.be/j9bYDjaAYzw?t=1420
Correção:

Enunciado:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

print('====== Desafio 43 ======')

p = float(input('Insira o peso: '))
a = float(input('Insira a altura: '))

imc = p / (a ** 2)

if imc < 18.5:
    print('IMC = {:.1f} => Abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC = {:.1f} => Peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC = {:.1f} => Sobrepeso.'.format(imc))
elif imc >=30 and imc < 40:
    print('IMC = {:.1f} => Obesidade.'.format(imc))
else:
    print('IMC = {:.1f} => Obesidade mórbida.'.format(imc))
