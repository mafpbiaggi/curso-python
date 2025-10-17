# Desafio 3: https://youtu.be/31llNGKWDdo?si=rEhVWGcuLVID6MdP
# Crie um script Python que leia dois números e tente mostrar a soma entre eles.
# Saída esperada: A soma é %resultado%.

# Exibe o cabeçalho
print("====== Desafio 3 ======")

# Recebe os valores digitado pelo usuário, já em formato numérico utilizando a função int()
num1 = int(input("Primeiro número:"))
num2 = int(input("Segundo número:"))

# Exibe o resultado com a conta sendo feita na mesma linha.
print("A soma é", (num1+num2))

# É possível indexar quais os valores a serem exibidos
# resultado = num1 + num2
# print('A soma entre {0} e {1} é igual a {2}'.format(num1, num2, resultado))