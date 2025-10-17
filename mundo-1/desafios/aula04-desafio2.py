# Desafio 2: https://youtu.be/31llNGKWDdo?si=rEhVWGcuLVID6MdP
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
# Exemplo da saída: "Você nasceu no dia 17 de Mar de 1978."

# Exibe o cabeçalho
print("====== Desafio 2 ======")

# Coleta os dados do usuário e os armazena em variáveis
dia = input("Dia = ")
mes = input("Mês = ")
ano = input("Ano = ")

# Exibe a resposta na tela
print("Você nasceu no dia", dia, "de", mes, "de", ano + ".")

# Outra forma de exibir (mostrado pelo Gustavo em aula)
# print('Olá {}! É um prazer te conhecer.'.format(nome))