# Exercício 4: https://youtu.be/tHYxjJxtJko?si=EoUaRK3R75Si04Gi
# Crie um programa que receba um valor do usuário e retorne informações sobre o conteúdo digitado
# Saídas esperadas:

## O tipo primitivo desse valor é %
## Só tem espaços?
## É um número?
## É alfabético?
## Está em letras maiúsculas?
## Está em letras minúsculas?
## Está capitalizada (Primeira maiúscula)?

n = input("Digite qualquer coisa: ")

print('O tipo primitivo do valor digitado é', type(n))
print('Só tem espaços? Resposta:', n.isspace())
print('É um número? Resposta:', n.isnumeric())
print('É alfabético? Resposta:', n.isalpha())
print('Está em letras maiúsculas? Resposta:', n.isupper())
print('Está em letras minúsculas? Resposta:', n.islower())
print('Está captalizado (Primeira maiúscula)? Resposta:', n.istitle())