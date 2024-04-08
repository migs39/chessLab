import pygame
import CL_game as game
import CL_menus as menus
import CL_colors as clr
import CL_mqtt as mqtt
import CL_scores as scores
from CL_utils import randomSquare as R
def main():
    
    pygame.init()

    #criando a tela a
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    #tamanho do tabuleiro
    x, y = 720, 720
    #posição inicial para deixar o tabuleiro centralizado
    #x_0 = (screenWidth - x)//2
    x_0 = 40
    y_0 = (screenHeight - y)//2
    mqtt.msgOut('002')
    pygame.display.set_caption("ChessLab")
    while True:
        screen.fill(clr.background2)
        configValues = (screen, clr.background2, 96, 96, 48, 96, 294, 48, 240, 176, 408, 176, 576, 176, 56,
        16, 8, 240, 374, 408, 374, 576, 374, 56, 16, 8, 800, 680, 64, 16, 8, 96, 492,
        48, 248, 572, 480, 572, 48, 16, 8, 96, 8, 32, 16, 8, 0, '15 s', '30 s', '45 s',
        '30 s', '0 s', '1 s', '2 s', '1 s', clr.white, clr.aqua)
        T, D, M = (menus.mainMenu(configValues, screen, 500, 80, 160, 256, 520, 344, 720, 384, 40, 720, 464, 40, 720, 544,
                40, 720, 624, 48, 16, 8, clr.white, clr.background2))
        screen.fill(clr.background2)
        #print(D)
        mqtt.msgOut("001")
        #print("chegou aq ")


        Squares = []
        for i in range(3):
            #mqtt.sqrIn()
            Squares.append(mqtt.sqrIn())
            #Squares.append(utils.randomSquare())

        if M == 0:
            points = (game.CL_game(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 80, 48, 40, 784, 520, 872, 520, 936, 520, clr.bwhite, 
            clr.bblack, clr.white, None, clr.green, T, Squares[2], Squares[2], Squares[2], clr.background2, 0, D))
        elif M == 1:
            points = (game.CL_game_R(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 784, 520, 80, 
                clr.bwhite, clr.bblack, clr.white, Squares[2], Squares[2], Squares[2],
                clr.aqua, T, clr.background2, 0, D))
        mqtt.msgOut('002')
        if T == 15:
            Tc = 0
        if T == 30:
            Tc = 1
        if T == 45:
            Tc = 2
        if scores.isHighscore(M, Tc, D, scores.scoresFile, scores.namesFile, points):
            menus.wFinalScreen(screen, points, clr.background2, M, Tc, D)
        else:
            menus.finalScreen(screen, points, clr.background2, M, Tc, D)



def mainTest():
    
    pygame.init()

    #criando a tela a
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    #tamanho do tabuleiro
    x, y = 720, 720
    #posição inicial para deixar o tabuleiro centralizado
    #x_0 = (screenWidth - x)//2
    x_0 = 40
    y_0 = (screenHeight - y)//2
    pygame.display.set_caption("ChessLab")
    while True:
        screen.fill(clr.background2)
        #mqtt.msgOut('002')
        configValues = (screen, clr.background2, 96, 96, 48, 96, 294, 48, 240, 176, 408, 176, 576, 176, 56,
        16, 8, 240, 374, 408, 374, 576, 374, 56, 16, 8, 800, 680, 64, 16, 8, 96, 492,
        48, 248, 572, 480, 572, 48, 16, 8, 96, 8, 32, 16, 8, 0, '15 s', '30 s', '45 s',
        '30 s', '0 s', '1 s', '2 s', '1 s', clr.white, clr.aqua)
        T, D, M = (menus.mainMenu(configValues, screen, 500, 80, 160, 256, 520, 344, 720, 384, 40, 720, 464, 40, 720, 544,
                40, 720, 624, 48, 16, 8, clr.white, clr.background2))
        print(M)
        screen.fill(clr.background2)
        #print(D)
        #mqtt.msgOut("001")
        #print("chegou aq ")


        Squares = []
        for i in range(3):
            #mqtt.sqrIn()
            #Squares.append(mqtt.sqrIn())
            Squares.append(R())
        print(M)
        if M == 0:
            points = (game.CL_game_test(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 80, 48, 40, 784, 520, 872, 520, 936, 520, clr.bwhite, 
            clr.bblack, clr.white, None, clr.green, T, Squares[2], Squares[2], Squares[2], clr.background2, 0, D))
        elif M == 1:
            print('a')
            points = (game.CL_game_R_test(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 784, 520, 80, 
                clr.bwhite, clr.bblack, clr.white, Squares[2], Squares[2], Squares[2],
                clr.aqua, T, clr.background2, 0, D))
        #mqtt.msgOut('002')
        if T == 15:
            Tc = 0
        if T == 30:
            Tc = 1
        if T == 45:
            Tc = 2
        if scores.isHighscore(M, Tc, D, scores.scoresFile, scores.namesFile, points):
            menus.wFinalScreen(screen, points, clr.background2, M, Tc, D)
        else:
            menus.finalScreen(screen, points, clr.background2, M, Tc, D)



if __name__ == '__main__':
    mainTest()

