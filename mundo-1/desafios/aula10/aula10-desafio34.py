# Desafio 34: https://youtu.be/K10u3XIf1-Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1834
# Correção: https://youtu.be/Sfadj_AzKHw

# Enunciado:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('====== Desafio 34 ======')

s = float(input('Insira o valor do salário: R$ '))
a = 15

if s > 1250:
    a = 10

print('Salário atual: R$ {:.2f} | Aumento aplicado: {}%'.format(s, a))
print('Salário aumentado: R$ {:.2f}'.format(s + (s * a/100)))

# Solução do professor:
'''
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
'''
