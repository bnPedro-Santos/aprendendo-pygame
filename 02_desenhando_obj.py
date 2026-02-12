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
    
    #desenhando formas
    #display, (r,g,b), x, y, larg, h)
    pygame.draw.rect(tela, (255,0,0), (200, 300,40,50))
    #display, (r,g,b), (x,y), raio)
    pygame.draw.circle(tela,(0,0,255), (300,260), 40)
    #display, (r,g,b), (x,y), (pos inicio),(pos fim), espessura)
    pygame.draw.line(tela,(255,255,0),(390,0),(360,600),10)

    pygame.display.update() #atualiza os quadros do jogo

