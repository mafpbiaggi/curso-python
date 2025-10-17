# Desafio 10: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1991
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação do Dólar: R$ 3,27

# Cabeçalho
print ('====== Desafio 10 =======\n')

# Recebe valor
n = float(input('Digite o valor em dinheiro para conversão: '))

# Calcula conversão Reais em Dólar
dol = n / 3.27

# Exibe resultado
print('Você tem R${:.2f}, portanto consegue comprar ${:.2f}.'.format(n, dol))