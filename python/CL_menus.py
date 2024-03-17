import pygame
import sys
import CL_game as game

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
aqua = (0, 255, 255) 

def write_topmid(x_c, y_0, fontSize, screen, text, color = black, inflationx = 0, inflationy = 0):
    font = pygame.font.Font(None, fontSize)
    display = font.render(text, True, color)
    displayRect = display.get_rect()
    displayRect.midtop = (x_c, y_0)
    screen.blit(display, displayRect)
    finalRect = displayRect.inflate(inflationx, inflationy)
    finalRect.center = displayRect.center
    pygame.display.flip()
    return(finalRect)



def mainMenu(screen, xcTitle, yTitle, fTitle, xcBoard, ycBoard, lenghtBoard, xcPlay,
             yPlay, fPlay, xcRecords, yRecords, fRecords, xcCredits, yCredits,
             fCredits, xcQuit, yQuit, fQuit, xInf, yInf, dfColor, c1, c2, bgColor):
    screen.fill(bgColor)
    running = True
    while running:
        #escreve o Titulo
        write_topmid(xcTitle, yTitle, fTitle, screen, 'Chess Lab', dfColor)
        #desenha o tabuleiro
        xBoard = xcBoard - lenghtBoard/2
        yBoard = ycBoard - lenghtBoard/2
        game.drawBoard(xBoard, yBoard, lenghtBoard, lenghtBoard, screen, c1, c2, None)

        #cria os botões
        buttons = []
        playButton = write_topmid(xcPlay, yPlay, fPlay, screen, 'Jogar', dfColor, xInf, yInf)
        buttons.append(playButton)

        RecordsButton = write_topmid(xcRecords, yRecords, fRecords, screen, 'Melhores Pontuações', dfColor, xInf, yInf)
        buttons.append(RecordsButton)

        CreditsButton = write_topmid(xcCredits, yCredits, fCredits, screen, 'Créditos', dfColor, xInf, yInf)
        buttons.append(CreditsButton)

        QuitButton = write_topmid(xcQuit, yQuit, fQuit, screen, 'Sair', dfColor, xInf, yInf)
        buttons.append(QuitButton)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    for button in buttons:
                        if (button.left < mx < button.right) and (button.top < my < button.bottom):
                            if button == playButton:
                                screen.fill(bgColor)
                                configMenu(screen, bgColor, 96, 96, 64, 96, 336, 64, 240, 240, 408, 240, 576, 240, 56,
                                           16, 8, 240, 472, 408, 472, 576, 472, 56, 16, 8, 800, 680, 72, 16, 8)
                                
        pygame.display.flip()
    sys.exit()

def configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y, tf,
                tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                startInfy, t1 = '15', t2 = '30', t3 = '45', T = '30', d1 = '0', d2 = '1', d3 = '2', D = '1',
                dfColor = white, spColor = aqua):
    
    if not T in [t1, t2, t3]:
        raise TypeError('Tempo selecionado não disponível')
    if not D in [d1, d2, d3]:
        raise TypeError('Decremento selecionado não disponível')
    
    running = True
    while running:
        #escrevendo os titulos
        game.write(tTitlex, tTitley, tTitlef, screen, "Selecione o tempo:", dfColor)
        game.write(dTitlex, dTitley, dTitlef, screen, "Selecione o decremento:", dfColor)


        #Escrevendo os botoes
        Buttons = []

        if T == t1:
            color = spColor
        else:
            color = dfColor
        t1Button = write_topmid(t1x_c,t1y, tf, screen, t1, color, tinfx, tinfy)
        Buttons.append(t1Button)

        if T == t2:
            color = spColor
        else:
            color = dfColor
        t2Button = write_topmid(t2x_c,t2y, tf, screen, t2, color, tinfx, tinfy)
        Buttons.append(t2Button)

        if T == t3:
            color = spColor
        else:
            color = dfColor
        t3Button = write_topmid(t3x_c,t3y, tf, screen, t3, color, tinfx, tinfy)
        Buttons.append(t3Button)


        if D == d1:
            color = spColor
        else:
            color = dfColor
        d1Button = write_topmid(d1x_c, d1y, df, screen, d1, color, dinfx, dinfy)
        Buttons.append(d1Button)
        
        if D == d2:
            color = spColor
        else:
            color = dfColor
        d2Button = write_topmid(d2x_c, d2y, df, screen, d2, color, dinfx, dinfy)
        Buttons.append(d2Button)

        if D == d3:
            color = spColor
        else:
            color = dfColor
        d3Button = write_topmid(d3x_c, d3y, df, screen, d3, color, dinfx, dinfy)
        Buttons.append(d3Button)

        
        startButton = write_topmid(startx_c, starty, startf, screen, 'Começar', dfColor, startInfx, startInfy)
        Buttons.append(startButton)

        #conferindo eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    for button in Buttons:
                        if (button.left < mx < button.right) and (button.top < my < button.bottom):
                            if button == startButton:
                                print('Play')
                            if button == t1Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, t1, d1, d2, d3, D, dfColor, spColor)
                            if button == t2Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, t2, d1, d2, d3, D, dfColor, spColor)
                            if button == t3Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, t3, d1, d2, d3, D, dfColor, spColor)
                            
                            if button == d1Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, T, d1, d2, d3, d1, dfColor, spColor)
                        
                            if button == d2Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, T, d1, d2, d3, d2, dfColor, spColor)

                            if button == d3Button:
                                return configMenu(screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c,
                                                t1y, t2x_c, t2y, t3x_c, t3y, tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y,
                                                d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                                                startInfy, t1, t2, t3, T, d1, d2, d3, d3, dfColor, spColor)
        pygame.display.flip()
    sys.exit()







def main():
    
    pygame.init()

    #criando a tela
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")
    #configMenu(screen, 96, 96, 64, 96, 336, 64, 240, 240, 408, 240, 576, 240, 56,
    #               16, 8, 240, 472, 408, 472, 576, 472, 56, 16, 8, 800, 680, 72, 16, 8)
    mainMenu(screen, 500, 80, 240, 256, 520, 344, 720, 384, 64, 720, 464, 64, 720, 544,
             64, 720, 624, 64, 16, 8, white, bbwhite, bbblack, background2)

if __name__ == '__main__':
    main()