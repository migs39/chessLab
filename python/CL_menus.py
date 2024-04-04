import pygame
import sys
import CL_utils as utils
import CL_colors as clr







def mainMenu(configMenuValues, screen, xcTitle, yTitle, fTitle, xcBoard, ycBoard, lenghtBoard, xcPlay,
             yPlay, fPlay, xcRecords, yRecords, fRecords, xcCredits, yCredits,
             fCredits, xcQuit, yQuit, fQuit, xInf, yInf, dfColor, bgColor):
    mainMenuValues = (screen, xcTitle, yTitle, fTitle, xcBoard, ycBoard, lenghtBoard, xcPlay,
                        yPlay, fPlay, xcRecords, yRecords, fRecords, xcCredits, yCredits,
                        fCredits, xcQuit, yQuit, fQuit, xInf, yInf, dfColor, bgColor)
    screen.fill(bgColor)
    running = True
    while running:
        # Escreve o Título
        utils.write_topmid(xcTitle, yTitle, fTitle, screen, 'Chess Lab', dfColor, clr.background2, font = utils.titleFont)
        # Desenha o tabuleiro
        xBoard = xcBoard - lenghtBoard/2
        yBoard = ycBoard - lenghtBoard/2
        utils.drawBoard(xBoard, yBoard, lenghtBoard, lenghtBoard, screen, clr.bwhite, clr.bblack, None)

        # Cria os botões
        buttons = []
        playButton = utils.write_topmid(xcPlay, yPlay, fPlay, screen, 'Jogar', dfColor, clr.background2, xInf, yInf, font = utils.buttonFont)
        buttons.append(playButton)

        recordsButton = utils.write_topmid(xcRecords, yRecords, fRecords, screen, 'Melhores Pontuações', dfColor, clr.background2, xInf, yInf, font = utils.buttonFont)
        buttons.append(recordsButton)

        creditsButton = utils.write_topmid(xcCredits, yCredits, fCredits, screen, 'Créditos', dfColor, clr.background2, xInf, yInf, font = utils.buttonFont)
        buttons.append(creditsButton)

        quitButton = utils.write_topmid(xcQuit, yQuit, fQuit, screen, 'Sair', dfColor, clr.background2, xInf, yInf, font = utils.buttonFont)
        buttons.append(quitButton)

        boardButton = pygame.Rect(xBoard, yBoard, lenghtBoard, lenghtBoard)
        buttons.append(boardButton)

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
                                #return configMenu(screen, bgColor, 96, 96, 48, 80, 336, 48, 240, 224, 408, 224, 576, 224, 56,
                                #           16, 8, 240, 456, 408, 456, 576, 456, 56, 16, 8, 800, 680, 40, 16, 8)
                                return(configMenu(mainMenuValues, *configMenuValues))
                            if button == boardButton:
                                clr.switchcolor()
                                return mainMenu(screen, xcTitle, yTitle, fTitle, xcBoard, ycBoard, lenghtBoard, xcPlay,
                                                yPlay, fPlay, xcRecords, yRecords, fRecords, xcCredits, yCredits,
                                                fCredits, xcQuit, yQuit, fQuit, xInf, yInf, dfColor, bgColor)
                            if button == quitButton:
                                running = False
                                
        pygame.display.flip()
    sys.exit()

def configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y, tf,
                tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx,
                startInfy, modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c, mode1y, modef, modeinfx, modeinfy,
                backx_c, backy, backf, backinfx, backinfy, mode = 0, t1 = '15 s', t2 = '30 s', t3 = '45 s', T = '30 s', d1 = '0 s',
                d2 = '1 s', d3 = '2 s', D = '1 s', dfColor = clr.white, spColor = clr.aqua):
    screen.fill(bgColor)
    configMenuValues = (screen, bgColor, tTitlex, tTitley, tTitlef, dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y, tf,
                        tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df, dinfx, dinfy, startx_c, starty, startf, startInfx, backx_c,
                        backy, backf, backinfx, backinfy, mode, t1, t2, t3, T, d1, d2, d3, D, dfColor, spColor)
    if not T in [t1, t2, t3]:
        raise TypeError('Tempo selecionado não disponível')
    if not D in [d1, d2, d3]:
        raise TypeError('Decremento selecionado não disponível')
    if not mode in [0, 1]:
        raise TypeError('Modo não disponível')
    
    #screen.fill(bgColor)
    running = True
    while running:
        #escrevendo os titulos
        utils.write_topleft(tTitlex, tTitley, tTitlef, screen, "Selecione o tempo:", dfColor, clr.background2, font = utils.subtitleFont)
        utils.write_topleft(dTitlex, dTitley, dTitlef, screen, "Selecione o decremento:", dfColor, clr.background2, font = utils.subtitleFont)
        utils.write_topleft(modeTitlex, modeTitley, modeTitlef, screen, "Selecione o modo:", dfColor, clr.background2, font = utils.subtitleFont)


        #Escrevendo os botoes
        Buttons = []
        
        if T == t1:
            color = spColor
        else:
            color = dfColor
        t1Button = utils.write_topmid(t1x_c,t1y, tf, screen, t1, color, clr.background2, tinfx, tinfy, font = utils.infoFont)
        Buttons.append(t1Button)

        if T == t2:
            color = spColor
        else:
            color = dfColor
        t2Button = utils.write_topmid(t2x_c,t2y, tf, screen, t2, color, clr.background2, tinfx, tinfy, font = utils.infoFont)
        Buttons.append(t2Button)

        if T == t3:
            color = spColor
        else:
            color = dfColor
        t3Button = utils.write_topmid(t3x_c,t3y, tf, screen, t3, color, clr.background2, tinfx, tinfy, font = utils.infoFont)
        Buttons.append(t3Button)


        if D == d1:
            color = spColor
        else:
            color = dfColor
        d1Button = utils.write_topmid(d1x_c, d1y, df, screen, d1, color, clr.background2, dinfx, dinfy, font = utils.infoFont)
        Buttons.append(d1Button)
        
        if D == d2:
            color = spColor
        else:
            color = dfColor
        d2Button = utils.write_topmid(d2x_c, d2y, df, screen, d2, color, clr.background2, dinfx, dinfy, font = utils.infoFont)
        Buttons.append(d2Button)

        if D == d3:
            color = spColor
        else:
            color = dfColor
        d3Button = utils.write_topmid(d3x_c, d3y, df, screen, d3, color, clr.background2, dinfx, dinfy, font = utils.infoFont)
        Buttons.append(d3Button)

        if mode == 0:
            color = spColor
        else:
            color = dfColor
        mode0Button = utils.write_topmid(mode0x_c, mode0y, modef, screen, 'Clicar', color, clr.background2, modeinfx, modeinfy, font = utils.subtitleFont)
        Buttons.append(mode0Button)

        if mode == 1:
            color = spColor
        else:
            color = dfColor
        mode1Button = utils.write_topmid(mode1x_c, mode1y, modef, screen, 'Escrever', color, clr.background2, modeinfx, modeinfy, font = utils.subtitleFont)
        Buttons.append(mode1Button)

        startButton = utils.write_topmid(startx_c, starty, startf, screen, 'Começar', dfColor, clr.background2, startInfx, startInfy, font = utils.buttonFont)
        Buttons.append(startButton)

        backButton = utils.write_topmid(backx_c, backy, backf, screen, 'Voltar', dfColor, clr.background2, backinfx, backinfy, font = utils.buttonFont)
        Buttons.append(backButton)

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
                                return int(T[:2]), int(D[:2])
                            if button == backButton:
                                mainMenu(configMenuValues, *mainMenuValues)
                            if button == t1Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, t1, d1, d2, d3, D, dfColor,
                                                  spColor)
                            if button == t2Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, t2, d1, d2, d3, D, dfColor,
                                                  spColor)
                            if button == t3Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, t3, d1, d2, d3, D, dfColor,
                                                  spColor)
                            
                            if button == d1Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, T, d1, d2, d3, d1, dfColor,
                                                  spColor)
                        
                            if button == d2Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, T, d1, d2, d3, d2, dfColor,
                                                  spColor)

                            if button == d3Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, mode, t1, t2, t3, T, d1, d2, d3, d3, dfColor,
                                                  spColor)
                            if button == mode0Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, 0, t1, t2, t3, T, d1, d2, d3, D, dfColor,
                                                  spColor)
                            if button == mode1Button:
                                return configMenu(mainMenuValues, screen, bgColor, tTitlex, tTitley, tTitlef,
                                                  dTitlex, dTitley, dTitlef, t1x_c, t1y, t2x_c, t2y, t3x_c, t3y,
                                                  tf, tinfx, tinfy, d1x_c, d1y, d2x_c, d2y, d3x_c, d3y, df,
                                                  dinfx, dinfy, startx_c, starty, startf, startInfx, startInfy,
                                                  modeTitlex, modeTitley, modeTitlef, mode0x_c, mode0y, mode1x_c,
                                                  mode1y, modef, modeinfx, modeinfy, backx_c, backy, backf,
                                                  backinfx, backinfy, 1, t1, t2, t3, T, d1, d2, d3, D, dfColor,
                                                  spColor)
                            
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
    screen.fill(clr.background2)

    configValues = (screen, clr.background2, 96, 96, 64, 96, 336, 64, 240, 240, 408, 240, 576, 240, 56,
    16, 8, 240, 472, 408, 472, 576, 472, 56, 16, 8, 800, 680, 72, 16, 8, 96, 576,
    64, 256, 600, 408, 600, 56, 16, 8, 8, 8, 56, 16, 8, 0, '15 s', '30 s', '45 s',
    '30 s', '0 s', '1 s', '2 s', '1 s', clr.white, clr.aqua)
    print(mainMenu(configValues, screen, 500, 80, 160, 256, 520, 344, 720, 384, 40, 720, 464, 40, 720, 544,
             40, 720, 624, 48, 16, 8, clr.white, clr.background2))

if __name__ == '__main__':
    main()
