# Desafio 11: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2011
# Correção: https://youtu.be/mzSJpn9ldt4?si=b129IziXPTK0fz1y
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta
# uma área de 2m².

# Cabeçalho
print('====== Desafio 11 ======\n')

# Recebe valores do usuário
h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

# Calcula área e quantidade tinta.
a = h * l
t = a / 2

print('A parede tem uma área de {:.2f}m². Você precisa de {:.1f}l de tinta para pintá-la.'.format(a, t))