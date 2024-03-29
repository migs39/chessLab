import pygame
import CL_game as game
import CL_menus as menus
import CL_colors as clr
import CL_mqtt as mqtt

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
    pygame.display.set_caption("ChessLab")
    screen.fill(clr.background2)
    T, D = menus.mainMenu(screen, 500, 80, 240, 256, 520, 344, 720, 384, 64, 720, 464, 64, 720, 544,
             64, 720, 624, 64, 16, 8, clr.white, clr.background2)
    screen.fill(clr.background2)
    mqtt.msgOut("001")
    print("chegou aq ")

    Squares = []
    for i in range(3):
        Squares.append(mqtt.sqrIn())
    print("chegou aq ")


    game.CL_game(x_0, y_0, x, y, 775, 300, 120, 0, 0, 100, screen, 100, 70, 50, 784, 464, 872, 464, 936, 464, clr.bwhite, 
            clr.bblack, clr.white, None, clr.green, T, Squares[0], Squares[1], Squares[2], clr.background2, 0, D)    

if __name__ == '__main__':
    main()



