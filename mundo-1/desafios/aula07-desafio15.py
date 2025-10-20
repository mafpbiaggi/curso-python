# Exercício 15: https://youtu.be/I4NYUeetLAc?si=G5OTvuA1YDfE1z6o
# Observação: Esse exercício não estava presente no vídeo da aula 07 como desafio,
# mas está presente na playlist de exercícios considerando o conteúdo apresentado até a aula 07.

# Enunciado:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('====== Desafio 15 ======')

km = float(input('Insira a quantidade de km rodados pelo carro: '))
d = int(input('Insira a quantidade de diárias de locação: '))

subtotal_km = km * 0.15
subtotal_d = d * 60

print('Dados de cobrança: {}km rodados -> {} diárias'.format(km, d))
print('O valor a ser pago é de R${:.2f}'.format(subtotal_km + subtotal_d))

# Sugestão de solução do professor:

# dias = int(input('Quantos dias alugados?'))
# km = float(input('Quantos Km rodados?'))
# pago = (dias * 60) + (km * 0.15)
# print('O total a pagar é de R${:.2f}'.format(pago))

