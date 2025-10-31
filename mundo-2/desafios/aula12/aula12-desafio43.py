"""
Desafio 43: https://youtu.be/j9bYDjaAYzw?t=1420
Correção: https://youtu.be/b7r34za963I

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

'''
# Solução do professor:
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
'''
