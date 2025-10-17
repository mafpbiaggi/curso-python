# Desafio 8: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1945
# Correção: https://youtu.be/KjcdG05EAZc?si=znqVlpyJ3Xk4QmTY
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Cabeçalho
print('====== Desafio 8 ======\n')

# Recebe valor em float, pois o usuário pode digitar 2.35, por exemplo
m = float(input('Digite um valor em metros: '))

# Calcula a conversão
cm = m * 100
mm = m * 1000

# Durante a aula de correção, foi proposto nosso programa converta metros para outras unidades de medida:
# km - kilômetros
# hm - hequitômetros
# dam - decâmetros
# dm - decímetros

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10

print('Conversor de medidas (m -> km, hm, dam, dm, cm, mm)')
print('Valor digitado: {:.2f}m'.format(m))
print('{:.2f}m -> {:.3f}km'.format(m, km))
print('{:.2f}m -> {:.2f}hm'.format(m, hm))
print('{:.2f}m -> {:.2f}dam'.format(m, dam))
print('{:.2f}m -> {:.0f}dm'.format(m, dm))
print('{:.2f}m -> {:.0f}cm'.format(m, cm))
print('{:.2f}m -> {:.0f}mm'.format(m, mm))


