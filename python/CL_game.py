import pygame
import sys
import CL_utils as utils
import CL_colors as clr
import CL_mqtt as mqtt

def showMoves(sq1, x1, y1, f1, sq2, x2, y2, f2, sq3, x3, y3, f3, screen, color=clr.black, bg = clr.background2, font = utils.infoFont):
    utils.write_midleft(x1, y1, f1, screen, sq1, color, bg, 8, 8, font)
    #utils.write_midleft(x2, y2, f2, screen, sq2, color, bg, 8, 8, font)
    #utils.write_midleft(x3, y3, f3, screen, sq3, color, bg, 8, 8, font)

def showTimer(x_0, y_0, fontSize, screen, time=30, color=clr.black, bg = clr.background2, font = utils.infoFont):
    return utils.write_topleft(x_0, y_0, fontSize, screen, "{:.1f}".format(time), color, bg, 0, 0, font)

def CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen, fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y,
            c1=clr.bwhite, c2=clr.bblack, cDf=clr.black, highlight=None, hlColor=clr.red, time=30.0, sq1="", sq2="", sq3="",
            bgColor=clr.background2, points = 0, decrease = 1):
    utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    running = True
    timeRemaining = time
    showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf, bgColor)
    clock = pygame.time.Clock()
    textRect = pygame.Rect(x_0+x, 0, screen.get_width() - x_0 - x, screen.get_height())
    pygame.display.flip()
    while running:
        screen.fill(bgColor, textRect)
        showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf, bgColor)
        showMoves(sq1, sq1x, sq1y, fsq1, sq2, sq2x, sq2y, fsq2, sq3, sq3x, sq3y, fsq3, screen, cDf, bgColor)
        utils.write_topleft(px_0, py_0, pFontSize, screen, str(points), cDf, bgColor, 0, 0, utils.infoFont)
        # Desenhar o tabuleiro por último
        utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
        timeRemaining -= 1 / 60
        if timeRemaining<=0: #Fim de jogo
            mqtt.msgOut('112')
            return(points)
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
                        mqtt.sqrOut(name)
                        acertou = mqtt.msgIn()
                        acertou = int(acertou)
                        if acertou:
                            sqNew = mqtt.sqrIn() #Espera 2 numeros de 1 a 8 representando o quadrado no final da memoria
                            #return CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen,
                            #                fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y, c1, c2, cDf,
                            #                highlight, hlColor, timeRemaining, sq2, sq3, sqNew, bgColor, points+1)
                            return CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen,
                                            fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y, c1, c2, cDf,
                                            highlight, hlColor, timeRemaining, sqNew, sqNew, sqNew, bgColor, points+1)

                        elif not acertou:
                            return CL_game(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen,
                                            fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y, c1, c2, cDf,
                                            highlight, hlColor, timeRemaining - decrease, sq1, sq2, sq3, bgColor, points)
        pygame.display.flip()


def CL_game_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen, fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y,
            c1=clr.bwhite, c2=clr.bblack, cDf=clr.black, highlight=None, hlColor=clr.red, time=30.0, sq1="", sq2="", sq3="",
            bgColor=clr.background2, points = 0, decrease = 1):
    utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
    lines = ['8', '7', '6', '5', '4', '3', '2', '1']
    collumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    running = True
    timeRemaining = time
    showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf, bgColor)
    clock = pygame.time.Clock()
    textRect = pygame.Rect(x_0+x, 0, screen.get_width() - x_0 - x, screen.get_height())
    pygame.display.flip()
    while running:
        screen.fill(bgColor, textRect)
        showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf, bgColor)
        showMoves(sq1, sq1x, sq1y, fsq1, sq2, sq2x, sq2y, fsq2, sq3, sq3x, sq3y, fsq3, screen, cDf, bgColor)
        utils.write_topleft(px_0, py_0, pFontSize, screen, str(points), cDf, bgColor, 0, 0, utils.infoFont)
        # Desenhar o tabuleiro por último
        utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, highlight, hlColor)
        timeRemaining -= 1 / 60
        if timeRemaining<=0: #Fim de jogo
            #mqtt.msgOut('112')
            return(points)
        clock.tick(60)
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #mqtt.msgOut('002')
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    if x_0 <= mx <= x_0 + x and y_0 <= my <= x_0 + y:  # Se o click foi no tabuleiro
                        name = collumns[int((mx - x_0) // (x / 8))] + lines[int((my - y_0) // (y / 8))]
                        #mqtt.sqrOut(name)
                        #acertou = mqtt.msgIn() #Espera um bool acertou
                        acertou = name == sq1
                        if acertou:
                            #sqNew = mqtt.sqrIn() #Espera 2 numeros de 1 a 8 representando o quadrado no final da memoria
                            sqNew = utils.randomSquare()
                            return CL_game_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen,
                                            fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y, c1, c2, cDf,
                                            highlight, hlColor, timeRemaining, sq2, sq3, sqNew, bgColor, points+1)
                        elif not acertou:
                            return CL_game_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen,
                                            fsq1, fsq2, fsq3, sq1x, sq1y, sq2x, sq2y, sq3x, sq3y, c1, c2, cDf,
                                            highlight, hlColor, timeRemaining - decrease, sq1, sq2, sq3, bgColor, points)
        pygame.display.flip()


def CL_game_R_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen, ansx, ansy, ansf, 
              c1 = clr.bwhite, c2 = clr.bblack, cDf = clr.black, sq1 = 'a1', sq2 = 'b5', sq3 = 'e6',
              sq1color = clr.aqua, time = 30.0, bgColor = clr.background2, points = 0, decrease = 1):
    utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, sq1, sq1color)
    running = True
    timeRemaining = time
    showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
    clock = pygame.time.Clock()
    ans = ''
    textRect = pygame.Rect(x_0+x, 0, screen.get_width() - x_0 - x, screen.get_height())
    pygame.display.flip()
    while running:
        screen.fill(bgColor, textRect)
        showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
        utils.write_topleft(px_0, py_0, pFontSize, screen, str(points), cDf, bgColor, 0, 0, utils.infoFont)
        utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, sq1, sq1color)
        timeRemaining -= 1 / 60       
        if timeRemaining<=0: #Fim de jogo
            return(points)
        ansRect = utils.write_topleft(ansx, ansy, ansf, screen, ans, cDf, bgColor, 8, 8, utils.infoFont)        
        clock.tick(60)
        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Apaga o último caractere digitado
                    screen.fill(bgColor, ansRect)
                    ans = ans[:-1]
                elif len(ans) == 0 and event.key >= pygame.K_a and event.key <= pygame.K_h:
                    # Verifica se o primeiro caractere é uma letra do alfabeto
                    ans += chr(event.key).lower()
                elif len(ans) == 1 and event.key >= pygame.K_1 and event.key <= pygame.K_8:
                    # Verifica se o segundo caractere é um número de 1 a 8
                    ans += chr(event.key)
                elif event.key == pygame.K_RETURN and len(ans) == 2:
                    screen.fill(bgColor, ansRect)
                    if ans == sq1:
                        return CL_game_R_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize,
                                        screen, ansx, ansy, ansf, c1, c2, cDf, sq2, sq3, utils.randomSquare(), sq1color,
                                        timeRemaining, bgColor, points + 1, decrease)
                    else:
                        return CL_game_R_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize,
                                        screen, ansx, ansy, ansf, c1, c2, cDf, sq1, sq2, sq3, sq1color,
                                        timeRemaining - decrease, bgColor, points, decrease)
        pygame.display.flip()
                       
def CL_game_R(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize, screen, ansx, ansy, ansf, 
              c1 = clr.bwhite, c2 = clr.bblack, cDf = clr.black, sq1 = 'a1', sq2 = 'b5', sq3 = 'e6',
              sq1color = clr.aqua, time = 30.0, bgColor = clr.background2, points = 0, decrease = 1):
    utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, sq1, sq1color)
    running = True
    timeRemaining = time
    showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
    clock = pygame.time.Clock()
    ans = ''
    textRect = pygame.Rect(x_0+x, 0, screen.get_width() - x_0 - x, screen.get_height())
    pygame.display.flip()
    while running:
        screen.fill(bgColor, textRect)
        showTimer(tx_0, ty_0, tFontSize, screen, timeRemaining, cDf)
        utils.write_topleft(px_0, py_0, pFontSize, screen, str(points), cDf, bgColor, 0, 0, utils.infoFont)
        utils.drawBoard(x_0, y_0, x, y, screen, c1, c2, sq1, sq1color)
        timeRemaining -= 1 / 60       
        if timeRemaining<=0: #Fim de jogo
            mqtt.msgOut('112')
            return(points)
        utils.write_topleft(ansx, ansy, ansf, screen, ans, cDf, bgColor, 8, 8, utils.infoFont)        
        clock.tick(60)
        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Apaga o último caractere digitado
                    ans = ans[:-1]
                elif len(ans) == 0 and event.key >= pygame.K_a and event.key <= pygame.K_h:
                    # Verifica se o primeiro caractere é uma letra do alfabeto
                    ans += chr(event.key).lower()
                elif len(ans) == 1 and event.key >= pygame.K_1 and event.key <= pygame.K_8:
                    # Verifica se o segundo caractere é um número de 1 a 8
                    ans += chr(event.key)
                elif event.key == pygame.K_RETURN and len(ans) == 2:
                    mqtt.sqrOut(ans)
                    acertou = mqtt.msgIn()
                    if acertou:
                        return CL_game_R_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize,
                                        screen, ansx, ansy, ansf, c1, c2, cDf, sq2, sq3, mqtt.sqrIn(), sq1color,
                                        timeRemaining, bgColor, points + 1, decrease)
                    else:
                        return CL_game_R_test(x_0, y_0, x, y, tx_0, ty_0, tFontSize, px_0, py_0, pFontSize,
                                        screen, ansx, ansy, ansf, c1, c2, cDf, sq1, sq2, sq3, sq1color,
                                        timeRemaining - decrease, bgColor, points, decrease)
        pygame.display.flip()


def test():
    pygame.init()

    # Criando a tela
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")

    # Tamanho do tabuleiro
    x, y = 720, 720
    # Posição inicial para deixar o tabuleiro centralizado
    x_0 = 40
    y_0 = (screenHeight - y) // 2

    screen.fill(clr.background2)
    CL_game_test(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 80, 48, 40, 840, 520, 872, 520, 936, 520, clr.bwhite, 
                clr.bblack, clr.white, None, clr.green, 30, 'a1', 'b2', 'e4', clr.background2, 0, 0)   
    # Encerra o pygame
    pygame.quit()
    sys.exit()

def testR():
    pygame.init()

    # Criando a tela
    screenWidth, screenHeight = 1000, 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("ChessLab")

    # Tamanho do tabuleiro
    x, y = 720, 720
    # Posição inicial para deixar o tabuleiro centralizado
    x_0 = 40
    y_0 = (screenHeight - y) // 2

    screen.fill(clr.background2)
    print(CL_game_R_test(x_0, y_0, x, y, 784, 300, 96, 864, 192, 80, screen, 840, 464, 80, cDf=clr.white))


if __name__ == '__main__':
    testR()
