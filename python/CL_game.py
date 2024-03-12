import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)
background1 = (180, 180, 180)
#tabuleiro azul
bbwhite = (153, 217, 234)
bbblack = (63, 72, 204)
#tabuleiro de madeira
wbwhite = (185, 122, 87)
wbblack = (136, 0, 21)
#tabuleiro esverdeado
gbwhite = (239, 228,176)
gbblcak = (34, 177, 76)


def makeSqr(x_0, y_0, x, y, screen, color, name):
    #cria a casa
    sqr = pygame.Rect(x_0, y_0, x, y)
    #desenha a casa
    pygame.draw.rect(screen, color, sqr)

    

def drawBoard(x_0, y_0, x, y, screen, c1 = white, c2 = black):
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
            makeSqr(sqrX_0, sqrY_0, sqrX, sqrY, screen, color, name)
            if color == c1:
                color = c2
            elif color == c2:
                color = c1
    pygame.display.flip()

def showTimer(x_0, y_0, fontSize, screen, time = 30, color = black):
    font = pygame.font.Font(None, fontSize)
    display = font.render(str(time), True, color)
    displayRect = display.get_rect()
    displayRect.topleft = (x_0, y_0)
    screen.blit(display, displayRect)
    pygame.display.flip()
    
def CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, screen, c1 = white, c2 = black):
    drawBoard(x_0, y_0, x, y, screen, c1, c2)
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
    running = True
    while running:
        showTimer(tx_0, ty_0, tFontSize, screen)
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
    screenWidth, screenHeight = 800, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")

    clock = pygame.time.Clock()

    #tamanho do tabuleiro
    x, y = 720, 720
    #posição inicial para deixar o tabuleiro centralizado
    x_0 = (screenWidth - x)//2
    y_0 = (screenHeight - y)//2


    screen.fill(background1)
    CL_game(x_0, y_0, x, y, x_0, 10, 40, screen, wbwhite, wbblack)

    # Encerra o pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
