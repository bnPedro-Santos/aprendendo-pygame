import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#criando Display

x_tela = 640
y_tela = 480

x_move = 0
y_move = 0

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
    
    pygame.draw.rect(tela, (255,0,0), (x_move,y_move,40,50))

    if y_move >= y_tela:
        y_move = 0
    y_move += 1 #add 1 nas coord do retengulo


    pygame.display.update() #atualiza os quadros do jogo

