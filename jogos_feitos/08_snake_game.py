import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()

#musica
pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer_music.load('audio\music.wav')
pygame.mixer.music.play(-1) #começar a tocar a musica de novo
som_colisao = pygame.mixer.Sound('audio/Coin FX.wav')
# som_colisao.set_volume(0)



#criando Display

x_tela = 640
y_tela = 480

x_cobra = x_tela/2 #fica no meio da leta
y_cobra = y_tela/2 #fica no meio da leta

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0

tela = pygame.display.set_mode((x_tela ,y_tela))

pygame.display.set_caption('Jogo')#nome da tela
clock = pygame.time.Clock() #taxa de quadros
fonte = pygame.font.SysFont('arial', 40, True, True) #fonte, tamanho, negrito, italico


def aumenta_cobra(lista_cobra):
   for XeY in lista_cobra:
      pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))



def reiniciar_jogo():
    global pontos, comprimento_inicio, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicio = 2
    x_cobra = x_tela/2 #fica no meio da leta
    y_cobra = y_tela/2 #fica no meio da leta
    lista_cabeca = []
    lista_cobra = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
    

lista_cobra = []
comprimento_inicio = 2
morreu = False

#Todo jogo se passa dentro de um loop infinito
while True:
    clock.tick(30)
    tela.fill((170,170,170)) #preenchimento da tela
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0)) #texto, ant-alising

    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            exit()

        #controle parecido com o da cobrinha
        #Cada botão a cobrinha anda sem parar
        #não tem como apertar um botão na direçao contraria
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d: 
                if x_controle == velocidade:
                    pass
                else:    
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w: 
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s: 
                if y_controle == velocidade:
                    pass
                else:    
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle
    
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20)) 
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20)) 

    #criando colisão e aleatoriedade
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        som_colisao.play()

        comprimento_inicio += 1

    #fazendo a cobra crescer
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    #morte por cobra
    if lista_cobra.count(lista_cabeca) > 1:
        mensagem = "Perdeu!!!! Pressione R para jogar novamente"
        texto_formatado = fonte.render(mensagem, True, (0,0,0)) #texto, ant-alising
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((170,170,170))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (x_tela//2, y_tela//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    #cobra passar para o outro lado da tela
    if x_cobra > x_tela:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = x_tela
    if y_cobra > y_tela:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = y_tela


    if len(lista_cobra) > comprimento_inicio:
       del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    

    #
    tela.blit(texto_formatado, (450,40))
    pygame.display.update() #atualiza os quadros do jogo

