# Desafio 31: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1760
# Correção:

# Enunciado:
# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('====== Desafio 31 ======')

d = float(input('Qual é a distância da viagem? KM = '))
taxa = 0.50

if d > 200:
    taxa = 0.45

print('Distância da viagem: {} KM | Taxa/KM: R$ {:.2f}'.format(d, taxa))
print('Valor da passagem: R$ {:.2f}'.format(d*taxa))
