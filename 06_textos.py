import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()

#criando Display

x_tela = 640
y_tela = 480

x_move = x_tela/2 #fica no meio da leta
y_move = y_tela/2 #fica no meio da leta

x_blue = randint(40, 600)
y_blue = randint(50, 430)

pontos = 0

tela = pygame.display.set_mode((x_tela ,y_tela))

pygame.display.set_caption('Jogo')#nome da tela
clock = pygame.time.Clock() #taxa de quadros
fonte = pygame.font.SysFont('arial', 40, True, True) #fonte, tamanho, negrito, italico

#Todo jogo se passa dentro de um loop infinito

while True:
    clock.tick(30)
    tela.fill((0,0,0)) #preenchimento da tela
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255)) #texto, ant-alising

    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]:     
          x_move -= 15
        if pygame.key.get_pressed()[K_d]:     
          x_move += 15
        if pygame.key.get_pressed()[K_w]:     
          y_move -= 15 #valor de y é inverso
        if pygame.key.get_pressed()[K_s]:     
          y_move += 15 #valor de y é inverso
    
    ret_red = pygame.draw.rect(tela, (255,0,0), (x_move,y_move,40,50)) #retangulo verm
    ret_blue = pygame.draw.rect(tela, (0,0,255), (x_blue,y_blue,40,50)) #retangulo azul

    #criando colisão
    if ret_red.colliderect(ret_blue):
      x_blue = randint(40, 600)
      y_blue = randint(50, 430)
      pontos += 1

    tela.blit(texto_formatado, (450,40))
    pygame.display.update() #atualiza os quadros do jogo

