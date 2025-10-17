# Desafio 5: https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1856
# Correção: https://www.youtube.com/watch?v=664e0G_S9nU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=13
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('====== Desafio 5 ======\n')
n = int(input('Digite um número inteiro: '))

a = n - 1
s = n + 1

print('O número digitado foi {}, portanto seu antecessor é {} e seu sucessor é {}'.format(n, a, s))

# Outra solução, sem uso de variáveis auxiliares:
# print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1))

# Essa possibilidade economiza memória, mas inviabiliza o uso dos recursos em caso futuro.
# Escolha com sabedoria.