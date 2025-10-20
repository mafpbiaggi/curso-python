# Desafio 19: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1781
# Correção: https://youtu.be/_Nk02-mfB5I?si=NAogI0eFAZr17VyD
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
print('====== Desafio 19 ======')

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

print('O aluno sorteado foi: {}'.format(choice([a1, a2, a3, a4])))