# Desafio 20: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1823
# Correção:
# O mesmo professor do desafio anterior  quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample
print('====== Desafio 20 ======')

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = sample([a1, a2, a3 ,a4], k=4)
print('A ordem de apresentação será: {}, {}, {} e {}'.format(lista[0], lista[1], lista[2], lista[3]))

'''A solução apresentada pelo professor envolve a função shuffle. Ela embaralha a lista original.
   Essa função atualiza a lista original. Por isso, preferi utilizar a função sample, pois ela não afeta o dado original.
   Veja a documentação: https://docs.python.org/pt-br/3.14/library/random.html#random.shuffle.
       
       Solução do professor:
       from random import shuffle
       [inputs ...]

       lista = [a1, a2, a3, a4]
       random.shuffle(lista)
       print('A ordem de apresentação será ')
       print(lista)

   
   Utilizei a exibição de cada item da lista separadamente no print para ocultar os colchetes e aspas.
   Caso contrário, a saída seria: ['<a1>', '<a2>', '<a3>', '<a4>']. Esse tipo de exibição não impacta no
   resultado, pois ele mostra os índices da lista já embaralhada.'''