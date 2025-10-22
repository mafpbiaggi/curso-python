# Desafio 29: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1718
# Correção:

# Enunciado:
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

v = int(input('Qual é a velocidade do veículo: KM/h = '))

if v > 80:
    multa = (v - 80) * 7.00
    print('Você foi multado.')
    print('Limite de velocidade: 80 KM/h | Velocidade registrada: {} KM/h'.format(v))
    print('Valor da multa: R$ {:.2f}'. format(multa))
