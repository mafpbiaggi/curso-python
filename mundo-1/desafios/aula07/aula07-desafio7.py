# Desafio 7: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1919
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('====== Desafio 7 ======\n')

print('Digite as notas do aluno (em caso de decimal, utilize ".")')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

print ('As notas do aluno foram:\nNota 1: {:.2f}\nNota2: {:.2f}\nMédia: {:.2f}'.format(n1, n2, media))

# Atenção ao uso de 1 casa decimal (:.1f), pois o Python arredonda para cima.