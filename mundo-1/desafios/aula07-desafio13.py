# Desafio 13: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2076
# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Cabeçalho
print('====== Desafio 13 ======\n')

# Recebe valor do salário
s = float(input('Digite o valor do salário do colaborador: '))

# Calcula reajuste para o novo salário
ns = s + (s * 0.15)

# Exibe o resultado
print('O valor do salário reajustado em 15% é de R${:.2f}.'.format(ns))