# Desafio 34: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1834
# Correção:

# Enunciado:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('====== Desafio 34 ======')

s = float(input('Insira o valor do salário: R$ '))
a = 15

if s > 1250:
    a = 10

print('Salário atual: R$ {:.2f} | Reajuste aplicado: {}%'.format(s, a))
print('Salário reajustado: R$ {:.2f}'.format(s + (s * a/100)))
