import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#criando Display

x_tela = 640
y_tela = 480

x_move = x_tela/2 #fica no meio da leta
y_move = y_tela/2 #fica no meio da leta

tela = pygame.display.set_mode((x_tela ,y_tela))

pygame.display.set_caption('Jogo')#nome da tela
clock = pygame.time.Clock() #taxa de quadros

#Todo jogo se passa dentro de um loop infinito

while True:
    clock.tick(30)
    tela.fill((0,0,0)) #preenchimento da tela
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            exit()

        #criando controles
        if pygame.key.get_pressed()[K_a]:     
          x_move -= 15
        if pygame.key.get_pressed()[K_d]:     
          x_move += 15
        if pygame.key.get_pressed()[K_w]:     
          y_move -= 15 #valor de y é inverso
        if pygame.key.get_pressed()[K_s]:     
          y_move += 15 #valor de y é inverso
    
    pygame.draw.rect(tela, (255,0,0), (x_move,y_move,40,50))

    pygame.display.update() #atualiza os quadros do jogo

