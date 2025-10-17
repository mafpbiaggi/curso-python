# Desafio 12: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2051
# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Cabeçalho
print('====== Desafio 12 =====\n')

# Recebe valor do salário
p = float(input('Digite o preço do produto: '))

# Calcula desconto
desc = p - (p * 0.05)

# Exibe o resultado
print('O preço do produto com desconto é R${:.2f}'.format(desc))