import pygame
import sys
from pygame import *

def print_res(x, y):
    score
    stri = "Set resistance value:  (Use the arrow keys to raise/low the bar)"
    fonte = pygame.font.Font.render(score, stri, True, (255, 255, 255))
    janela.blit(fonte, (x, y))

Amarelo = (255, 255, 0)
pygame.init()
pygame.font.init()
janela = pygame.display.set_mode((1200, 600))
back = pygame.transform.rotate(pygame.image.load('img_2.png'), 0)
display.set_caption('Projeto 1', 'Pc')
ver = 400
hor = 300
vel = 12
offset = [0, 0]
open_win = True
rot = 0
janela.blit(back, (0, 0))
conty = 300
contx = 135
default_res = 1
tecla = True
barfill = 0
score = pygame.font.Font("freesansbold.ttf", 32)
while open_win:
    pygame.time.delay(50)
    Rcl = False
    Lcl = False
    pygame.time.delay(5)
    # Sai do programa se QUIT ou pressionada a tecla escape
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                if barfill > 0:
                    barfill -= 1
            if event.key == K_RIGHT:
                if barfill < 10:
                    barfill += 1
                    draw = True
    janela.blit(back, (0, 0))
    if tecla:
        if conty < 510 and contx == 135:
            for i in range(11 - barfill):
                if (conty - 9 * i) > 210:
                    pygame.draw.circle(janela, Amarelo, (contx, conty - 9*i), 5)
            conty += 10
        elif contx < 700 and conty == 510:
            for i in range(11 - barfill):
                if (contx - 9 * i) > 130:
                    pygame.draw.circle(janela, Amarelo, (contx - 9 * i, conty), 5)
            contx += 10
        elif conty > 210:
            for i in range(11 - barfill):
                if (conty - 9 * i) > 210:
                    pygame.draw.circle(janela, Amarelo, (contx, conty - 9 * i), 5)
            conty -= 10
        else:
            for i in range(11 - barfill):
                if (contx - 9 * i) > 130:
                    pygame.draw.circle(janela, Amarelo, (contx - 9 * i, conty), 5)
            contx -= 10
    pygame.draw.rect(janela, Amarelo, (90, 80, 1000, 50), 20)

    pygame.draw.rect(janela, Amarelo, (90, 80, 100 * barfill, 50))
    pygame.draw.rect(janela, Amarelo, (90, 80, 1000, 50), 20)
    print_res(100, 30)
    pygame.display.update()
pygame.quit()
