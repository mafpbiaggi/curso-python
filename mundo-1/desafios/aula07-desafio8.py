# Desafio 8: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1945
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Cabeçalho
print('====== Desafio 8 ======\n')

# Recebe valor em float, pois o usuário pode digitar 2.35, por exemplo
m = float(input('Digite um valor em metros: '))

# Calcula a conversão
cm = m * 100
mm = m * 1000

# Exibe para o usuário as medidas em cm e mm
print('\nConversor de medidas:\n{:.2f}m -> {:.0f}cm\n{:.2f}m -> {:.0f}mm'.format(m, cm, m, mm))