# Desafio 29: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1718
# Correção: https://youtu.be/hgJ_ETNGSj8

# Enunciado:
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

v = int(input('Qual é a velocidade do veículo: KM/h = '))

if v > 80:
    print('Você foi multado.')
    print('Limite de velocidade: 80 KM/h | Velocidade registrada: {} KM/h'.format(v))

    multa = (v - 80) * 7.00
    print('Valor da multa: R$ {:.2f}'. format(multa))

# Solução do professor:
'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
'''
