"""
Desafio 44: https://youtu.be/j9bYDjaAYzw?t=1509
Correção:

Enunciado:
Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista cartão: 5% de desconto
- Parcelado cartão (2x): preço normal
- Parcelado cartão (3x ou mais): 20% de juros
"""

print('====== Desafio 44 ======')

pn = float(input('Digite o valor do produto: R$ '))
op = int(input('\nInforme a condição de pagamento\n1: À vista (dinheiro ou cheque)\n2: À vista (cartão)\n3: Parcelado no cartão (2x) ou\n4: Parcelado no cartão (+3x)\nOpção: '))

if op == 1:
    pf = pn - (pn * 0.10)
    desc_op = 'À vista (dinheiro ou cheque)'
elif op == 2:
    pf = pn - (pn * 0.05)
    desc_op = 'À vista cartão'
elif op == 3:
    pf = pn
    desc_op = 'Parcelado cartão (até 2x)'
elif op == 4:
    pf = pn + (pn * 0.20)
    desc_op = 'Parcelado cartão (+3x)'

print('\nValor do produto: R$ {:.2f}'.format(pn))
print('Opção de pagamento: {} => {}'.format(op, desc_op))
print('Valor do produto final: R$ {:.2f}'.format(pf))
