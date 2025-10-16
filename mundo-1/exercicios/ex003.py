# Exercício 3: https://youtu.be/hdDHg1p3YVc?si=Ejf4-TIWtAMPt1xN
# Crie um script Python que leia dois números e tente mostrar a soma entre eles.
# Saída esperada: A soma entre %num1% e %num2% é igual a %resultado%.

# Exibe o cabeçalho
print('====== Desafio 3 ======')

# Recebe os valores digitados pelo usuário, já em formato numérico utilizando a função int()
num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
resultado = num1 + num2

# Exibe o resultado utilizando o método .format() para organizar as variáveis a serem exibidas
print('A soma entre {} e {} é igual a {}'.format(num1, num2, resultado))

# É possível indexar quais os valores a serem exibidos
# print('A soma entre {0} e {1} é igual a {2}'.format(num1, num2, resultado))