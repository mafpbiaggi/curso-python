# Desafio 36: https://youtu.be/j9bYDjaAYzw?t=1024
# Correção: https://youtu.be/IV13X0QOMU8

# Enunciado:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quanto anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

print('====== Desafio 36 ======\n')

cor = {'0':'\033[m',
       'vm':'\033[31m',
       'vd':'\033[32m',
       'b':'\033[1m'}

v_casa = float(input('Digite o valor da casa: R$ '))
v_salario = float(input('Digite o valor do salário do comprador: R$ '))
q_anos = int(input('Em quantos anos deseja pagar? '))

q_parcelas = q_anos * 12
v_parcela = v_casa / q_parcelas

print('\n{}Avaliação de Crédito{}'.format(cor['b'], cor['0']))
print('Valor do Imóvel: R$ {:.2f}'.format(v_casa))
print('Salário: R$ {:.2f}'.format(v_salario))
print('Quantidade de parcelas: {}'.format(q_parcelas))
print('Valor da Parcela: R$ {:.2f}'.format(v_parcela))
print('=' * 30)

if v_parcela <= v_salario * 0.30:
    print('{}{}Empréstimo APROVADO{}'.format(cor['b'], cor['vd'], cor['0']))
else:
    print('{}{}Empréstimo REPROVADO{}'.format(cor['b'], cor['vm'], cor['0']))

'''
Solução do professor:

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = ' ')
print('a prestação será de R${:.2f}', format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO')
'''
