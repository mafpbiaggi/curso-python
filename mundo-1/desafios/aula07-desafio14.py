# Exercício 14: https://youtu.be/9l_Gay8BuAw?si=zJMLnrNze7F6wKO8
# Observação: Esse exercício não estava presente no vídeo da aula 07 como desafio,
# mas está presente na playlist de exercícios considerando o conteúdo apresentado até a aula 07.

# Enunciado:
# Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

print('====== Desafio 14 ======')

c = float(input('Digite o valor da temperatura: '))
f = c * 9 / 5 + 32
print('A temperatura {:.1f}°C convertida é {:.1f}°F.'.format(c, f))