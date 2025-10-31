"""
Desafio 44: https://youtu.be/j9bYDjaAYzw?t=1509
Correção: https://youtu.be/I-SH3QchuZ4

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

"""
# Solução professor:
print('{:=⁴0}'.format(' LOJAS GUANABARA'))
preço = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
"""
