import pygame
import CL_colors as clrs

import random
import os
import CL_mqtt as mqtt
fontsPath = os.path.join(os.path.dirname(__file__), '..', 'fonts')
#fontes
titleFont = os.path.join(fontsPath, 'title', 'IMFGPSC.ttf')
subtitleFont = os.path.join(fontsPath, 'subtitle', 'Aboreto.ttf') #V
infoFont = os.path.join(fontsPath, 'infos', 'Changa.ttf') #V
buttonFont = os.path.join(fontsPath, 'buttons', 'Aboreto.ttf')

#Funçoes de escrita
def write_topmid(x_c, y_0, fontSize, screen, text, color = clrs.white, bg = clrs.background2, inflationx = 0, inflationy = 0, font = None):
    fontR = pygame.font.Font(font, int(fontSize))
    display = fontR.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.midtop = (x_c, y_0)
    finalRect = displayRect.inflate(inflationx, inflationy)
    finalRect.center = displayRect.center
    screen.fill(bg, finalRect)
    screen.blit(display, displayRect)
    return(finalRect)

def write_topleft(x_0, y_0, fontSize, screen, text, color = clrs.white, bg = clrs.background2, inflationx = 0, inflationy = 0, font = None):
    fontR = pygame.font.Font(font, int(fontSize))
    display = fontR.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.topleft = (x_0, y_0)
    finalRect = displayRect.inflate(inflationx, inflationy)
    finalRect.center = displayRect.center
    screen.fill(bg, finalRect)
    screen.blit(display, displayRect)
    return(finalRect)

def write_midleft(x_0, y_c, fontSize, screen, text, color = clrs.white, bg = clrs.background2, inflationx = 0, inflationy = 0, font = None):
    fontR = pygame.font.Font(font, int(fontSize))
    display = fontR.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.midleft = (x_0, y_c)
    finalRect = displayRect.inflate(inflationx, inflationy)
    finalRect.center = displayRect.center
    screen.fill(bg, finalRect)
    screen.blit(display, displayRect)
    return(finalRect)

#------------------------------------------------------------------------------------

#Criação do tabuleiro
def makeSqr(x_0, y_0, x, y, screen, color):
    #cria a casa
    sqr = pygame.Rect(x_0, y_0, x, y)
    #desenha a casa
    pygame.draw.rect(screen, color, sqr)

def drawBoard(x_0, y_0, x, y, screen, c1 = clrs.white, c2 = clrs.black, highlight = None, hlColor = clrs.green):
    '''
    x e y são o tamanho do tabuleiro
    x_0 e y_0 são a posição do canto superior direito do tabuleiro
    screen é a tela em que o tabuleiro será desenhado
    '''
    sqrX, sqrY = x/8, y/8
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
    color = c1
    for line in range(8):
        if color == c1:
            color = c2
        elif color == c2:
            color = c1
        for collumn in range(8):
            sqrX_0 = x_0 + collumn*sqrX
            sqrY_0 = y_0 + line*sqrY
            name = collumns[collumn]+lines[line]
            if name == highlight:
                makeSqr(sqrX_0, sqrY_0, sqrX, sqrY, screen, hlColor)
            else:
                makeSqr(sqrX_0, sqrY_0, sqrX, sqrY, screen, color)
            if color == c1:
                color = c2
            elif color == c2:
                color = c1

def randomSquare():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numeros = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    primeiro_caracter = random.choice(letras)
    segundo_caracter = random.choice(numeros)
    sq = primeiro_caracter + segundo_caracter
    #print(sq)
    return sq