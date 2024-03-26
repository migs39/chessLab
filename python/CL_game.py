import pygame
import sys
import CL_utils as utils
import CL_colors as clr

def showMoves(sq1, x1, y1, f1, sq2, x2, y2, f2, sq3, x3, y3, f3, screen, color=clr.black):
    utils.write_midleft(x1, y1, f1, screen, sq1, color)
    utils.write_midleft(x2, y2, f2, screen, sq2, color)
    utils.write_midleft(x3, y3, f3, screen, sq3, color)

def showTimer(x_0, y_0, fontSize, screen, time=30, color=clr.black):
    return utils.write_topleft(x_0, y_0, fontSize, screen, "{:.1f}".format(time), color)

def CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, screen, fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y,
            c1=clr.white, c2=clr.black, cDf=clr.black, highlight=None, hlColor=clr.red, time=30.0, sq1="", sq2="", sq3="",
            bgColor=clr.background2):
    utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    running = True
    timeRemaining = time
    timerRect = showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
    clock = pygame.time.Clock()
    while running:
        screen.fill(bgColor, timerRect)
        timerRect = showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
        showMoves(sq1, sq1x, sq1y, fsq1, sq2, sq2x, sq2y, fsq2, sq3, sq3x, sq3y, fsq3, screen, cDf)
        # Desenhar o tabuleiro por último
        utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
        timeRemaining -= 1 / 60
        if timeRemaining<=0:
            return('end')
        clock.tick(60)
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if x_0 <= mx <= x_0 + x and y_0 <= my <= x_0 + y:  # Se o click foi no tabuleiro
                        name = collumns[int((mx - x_0) // (x / 8))] + lines[int((my - y_0) // (y / 8))]
                        print(name)
                        


def test():
    pygame.init()

    # Criando a tela
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")

    clock = pygame.time.Clock()

    # Tamanho do tabuleiro
    x, y = 720, 720
    # Posição inicial para deixar o tabuleiro centralizado
    x_0 = 40
    y_0 = (screenHeight - y) // 2

    screen.fill(clr.background2)
    CL_game(x_0, y_0, x, y, 775, 300, 120, screen, 100, 70, 50, 784, 464, 872, 464, 936, 464, clr.bwhite,
            clr.bblack, clr.white, None, clr.green, 30.0, 'a5', 'b6', 'e4')
    # Encerra o pygame
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    test()
