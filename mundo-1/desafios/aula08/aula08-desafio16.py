# Desafio 16: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1649
# Correção:https://youtu.be/-iSbDpl5Jhw?si=j1SIotbq_jxA4IXU

# Enunciado:
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex. Digite um número: 6.127 -> Saída: O número 6.127 tem a parte inteira 6.

from math import trunc
print('====== Desafio 16 ======')

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))

# Para adicionar um bloco inteiro de comentário, use ''' (três aspas seguidas)

'''É possível realizar esse mesmo resultado com uma função interna, sem importação
   print('O número {} tem a parte inteira {}'.format(n, int(n)))
   
   Nesse caso, a função int, retorna somente a parte inteira do número.'''