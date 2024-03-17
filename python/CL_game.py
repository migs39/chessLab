import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)
background1 = (180, 180, 180)
background2 = (48, 46, 43)
background3 = (60, 87, 60)
#tabuleiro azul
bbwhite = (153, 217, 234)
bbblack = (63, 72, 204)
#tabuleiro de madeira1
wbwhite = (185, 122, 87)
wbblack = (136, 0, 21)
#tabuleiro de madeira2
wbwhite2 = (255, 206, 158)
wbblack2 = (209, 139, 71)
#tabuleiro esverdeado
gbwhite = (239, 228,176)
gbblack = (34, 177, 76)

green = (0, 255, 0)
red = (255, 0, 0)


def makeSqr(x_0, y_0, x, y, screen, color, name):
    #cria a casa
    sqr = pygame.Rect(x_0, y_0, x, y)
    #desenha a casa
    pygame.draw.rect(screen, color, sqr)

    

def drawBoard(x_0, y_0, x, y, screen, c1 = white, c2 = black, highlight = None, hlColor = green):
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
                makeSqr(sqrX_0, sqrY_0, sqrX, sqrY, screen, hlColor, name)
            else:
                makeSqr(sqrX_0, sqrY_0, sqrX, sqrY, screen, color, name)
            if color == c1:
                color = c2
            elif color == c2:
                color = c1
    pygame.display.flip()

def write(x_0, y_0, fontSize, screen, text, color = black):
    font = pygame.font.Font(None, fontSize)
    display = font.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.topleft = (x_0, y_0)
    screen.blit(display, displayRect)
    pygame.display.flip()

def write_topmid(x_c, y_0, fontSize, screen, text, color = black):
    font = pygame.font.Font(None, fontSize)
    display = font.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.midtop(x_c, y_0)
    screen.blit(display, displayRect)
    pygame.display.flip()

def showMoves(sq1, x1, y1, f1, sq2, x2, y2, f2, sq3, x3, y3, f3, screen, color = black):
    write(x1, y1, f1, screen, sq1, color)
    write(x2, y2, f2, screen, sq2, color)
    write(x3, y3, f3, screen, sq3, color)

def showTimer(x_0, y_0, fontSize, screen, time = 30, color = black):
    write(x_0, y_0, fontSize, screen, str(time), color)     


def CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, screen, fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y,
            c1 = white, c2 = black, cDf = black, highlight = None, hlColor = red, time = 30.0, sq1 = "", sq2 = "", sq3 = ""):
    drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
    running = True
    while running:
        showTimer(tx_0, ty_0, tFontSize, screen, time, cDf)
        showMoves(sq1, sq1x, sq1y, fsq1, sq2, sq2x, sq2y, fsq2, sq3, sq3x, sq3y, fsq3, screen, cDf) 
            #eventos
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                   mx, my = pygame.mouse.get_pos()
                   if x_0<=mx<=x_0+x and y_0<=my<=x_0+y: #se o click foi no tabuleiro
                       name = collumns[int((mx-x_0)//(x/8))] + lines[int((my-y_0)//(y/8))]
                       print(name)
                   



def main():
    
    pygame.init()

    #criando a tela
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")

    clock = pygame.time.Clock()

    #tamanho do tabuleiro
    x, y = 720, 720
    #posição inicial para deixar o tabuleiro centralizado
    #x_0 = (screenWidth - x)//2
    x_0 = 40
    y_0 = (screenHeight - y)//2


    screen.fill(background2)
    CL_game(x_0, y_0, x, y, 775, 300, 120, screen, 100, 70, 50, 780, 450, 870, 465, 935, 475, wbwhite2, wbblack2, white, None, green,
            22.42, 'a5', 'b6', 'e4')

    # Encerra o pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
