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


global bwhite
global bblack


bblack = gbblack
bwhite = gbwhite


def switchcolor():
    global bwhite, bblack
    
    if (bwhite, bblack) == (bbwhite, bbblack):
        bwhite, bblack = wbwhite, wbblack
    elif (bwhite, bblack) == (wbwhite, wbblack):
        bwhite, bblack = wbwhite2, wbblack2
    elif (bwhite, bblack) == (wbwhite2, wbblack2):
        bwhite, bblack = gbwhite, gbblack
    elif (bwhite, bblack) == (gbwhite, gbblack):
        bwhite, bblack = white, black
    elif (bwhite, bblack) == (white, black):
        bwhite, bblack = bbwhite, bbblack