# Desafio 24: https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=2553
# Correção:https://youtu.be/QroT8cZMRnc?si=Xbf6y4qZfVv6Q405

# Enunciado:
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print('===== Desafio 24 ======')

cidade = str(input('Digite o nome de uma cidade: ')).strip()
filtra = cidade.split()

print('O nome da cidade é {}.'.format(cidade))
print('Ela começa com a palavra "santo"? R: {}'.format('santo' in filtra[0].lower()))

'''Sugestões do professor:
Utilize o método .split() na entrada da string para remover espaços antes e depois da palavra.

Solução do professor:

   cid = str(input('Digite a cidade que você nasceu: ')).strip()
   print(cid[:5].upper() == 'SANTO')
'''