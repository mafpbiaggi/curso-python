'''
Desafio 62: https://youtu.be/LH6OIn2lBaI?t=1928
Correção: https://youtu.be/BWAWq7n6PCk

Enunciado:
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('===== Desafio 62 ======')
print('Progressão Aritmética\n')

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = p

c = 1
print('PA = ', end='')

n = 10
t_term = 0
while n != 0:
    t_term += n
    while c <= t_term:
        print('{} '.format(t), end='')
        t += r
        c += 1
    print('-> Pausa')
    n = int(input('Quantos termos a mais você quer mostrar? '))
print('Finalizado')

# Observação: Tive muita dificuldade nesse exercício fui resolvendo junto com o processor durante a correção.

"""
# Solução do professor:
print('Gerado de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
"""
