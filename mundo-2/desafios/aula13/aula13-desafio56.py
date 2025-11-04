'''
Desafio 56: https://youtu.be/cL4YDtFnCt4?t=1964
Correção:

Enunciado:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    A média de idade do grupo;
    O nome do homem mais velho; e
    Quantas mulheres têm menos de 20 anos.
'''

print('===== Desafio 56 ======')
print('Pesquisa entre pessoas')

c = 0
soma = 0
m_velho = 0
n_velho = ''

for i in range(1, 5):
    print('\nDados da {}ª pessoa'.format(i))
    n = str(input('Digite o nome: ')).strip()
    i = int(input('Digite a idade (somente números): '))
    s = str(input('Digite o sexo (m, f): ')).strip()

    # Armazena as idades para calcular a média no final
    soma += i 

    # Verifica o sexo      
    if s == 'm':
        if i == 1:
            m_velho = i
            n_velho = n
        else:
            if i > m_velho:
                n_velho = n
    elif s == 'f':
        if i < 20:
            c += 1

print('\nEstatísticas ...')
print('A média de idade das pessoas é {:.2f}.'.format(soma/4))
print('O nome do homem mais velho é {}.'.format(n_velho.title()))
print('A quantidade de mulheres menores de 20 anos é {}.'.format(c))
