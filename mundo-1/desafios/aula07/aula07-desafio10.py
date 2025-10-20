# Desafio 10: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1991
# Correção: https://youtu.be/xM4AX3Lp2mo?si=K7NLODBxG8TJWF81
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação do Dólar: R$3,27 (Lançamento do curso - 2017)

# Cabeçalho
print ('====== Desafio 10 =======\n')

# Recebe valor
n = float(input('Digite o valor em dinheiro para conversão: '))

# Calcula conversão Reais em Dólar
dol = n / 5.41

# O professor sugeriu a implementação da conversão em Euro durante vídeo de correção
euro = n / 6.31

# Exibe resultado
print('Você tem R${:.2f}, portanto consegue comprar ${:.2f} e €{:.2f}.'.format(n, dol, euro))

# O programa teve os valores de cotação atualizadas.
# Hoje, 17/10/2025 está em R$5.41. Já o euro, custa R$6.31.