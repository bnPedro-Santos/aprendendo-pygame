import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#criando Display

x = 640
y = 480

tela = pygame.display.set_mode((x,y))

pygame.display.set_caption('Jogo')#nome da tela

#Todo jogo se passa dentro de um loop infinito

while True:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update() #atualiza os quadros do jogo

