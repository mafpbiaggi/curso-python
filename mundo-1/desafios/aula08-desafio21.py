# Desafio 21: https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1854
# Correção: https://youtu.be/9FiEji_fzvk?si=0vsk1dHbYGK32Ilp
# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

import pygame

pygame.init()
pygame.mixer.music.load('/home/suporte/Downloads/bom_grupo.mp3')
pygame.mixer.music.play()
input() # Comando sugerido pelos comentários do vídeo.
pygame.event.wait()

'''Não consegui realizar esse exercício, pois não quis procurar soluções prontas na internet,
   ou então, solicitar para IA gerar um código de solução. Portanto, a solução apresentada é
   do professor.
   
   No entanto, é necessário instalar a biblioteca. Não estou usando o PyCharm, então, instalei a lib
   manualmente no debian: sudo apt-get install python3-pygame'''