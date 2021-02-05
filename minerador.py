import pyautogui as auto
import keyboard as key
import time
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\Programas\pytesseract\tesseract.exe'
from PIL import Image

parar = True
    

def andar(x,y):
    mapa = auto.screenshot("mapa.png",region=(1260, 69, 120, 120))
    mapax, mapay = auto.locateCenterOnScreen("mapa.png")

    auto.moveTo(x, y)

    auto.moveTo(x-30,y) #esquerda
    auto.mouseDown(button = 'left')
    auto.mouseUp(button = 'left')
    lado = 'esquerdo'

    if((auto.locateCenterOnScreen("mapa.png")) != None):
        auto.moveTo(x+30,y-60) #cima
        auto.mouseDown(button = 'left')
        auto.mouseUp(button = 'left')
        lado = 'cima'
        
        if((auto.locateCenterOnScreen("mapa.png")) != None):
            auto.moveTo(x+90,y) #direita
            auto.mouseDown(button = 'left')
            auto.mouseUp(button = 'left')
            lado = 'direita'

            if((auto.locateCenterOnScreen("mapa.png")) != None):
                auto.moveTo(x+20,y+50) #baixo
                auto.mouseDown(button = 'left')
                auto.mouseUp(button = 'left')
                lado = 'baixo'

    minerar(lado)

#auto.moveTo(x-30,y-60) #esquerda cima
#auto.moveTo(x+90,y-60) #direita cima
#auto.moveTo(x+90,y+50) #direita baixo
#auto.moveTo(x-40,y+50) #esquerda baixo

def minerar(lado):
    x = 748
    y = 439 # centro
    auto.moveTo(x,y)
    time.sleep(2)

    if(lado == 'esquerdo'):
        auto.moveTo(x+70,y)
    elif(lado == 'cima'):
        auto.moveTo(x,y+50)
    elif(lado == 'direita'):
        auto.moveTo(x-70,y)
    elif(lado == 'baixo'):
        auto.moveTo(x,y-50)

    auto.keyDown('x')
    auto.keyUp('x')
    auto.mouseDown(button = 'left')
    auto.mouseUp(button = 'left')
    time.sleep(4)

def clicarBotao(botao):
    x,y = botao
    auto.moveTo(x,y)
    auto.mouseDown(button = 'left')
    auto.mouseUp(button = 'left')

def clicarBotao(botao):
    x,y = botao
    auto.moveTo(x,y)
    auto.mouseDown(button = 'left')
    auto.mouseUp(button = 'left')

    enviar = auto.locateCenterOnScreen("numero/botao/enviar.png", region=(615, 365, 200, 150), confidence = 0.9)
    if(enviar):
        x,y = enviar
        auto.moveTo(x,y)
        auto.mouseDown(button = 'left')
        auto.mouseUp(button = 'left')

def validar():
    #quantidade += 1
    #print(quantidade)
    # zero
    zero = auto.locateOnScreen("numero/0.png", region=(615, 365, 200, 150), confidence = 0.7)
    zeroDois = auto.locateOnScreen("numero/0 2.png", region=(615, 365, 200, 150), confidence = 0.7)

    # um
    um = auto.locateOnScreen("numero/1.png", region=(615, 365, 200, 150), confidence = 0.7)
    umDois = auto.locateOnScreen("numero/1 2.png", region=(615, 365, 200, 150), confidence = 0.7)
    umTres = auto.locateOnScreen("numero/1 3.png", region=(615, 365, 200, 150), confidence = 0.7)

    # dois
    dois = auto.locateOnScreen("numero/2.png", region=(615, 365, 200, 150), confidence = 0.7)
    doisDois = auto.locateOnScreen("numero/2 2.png", region=(615, 365, 200, 150), confidence = 0.7)

    # tres
    tres = auto.locateOnScreen("numero/3.png", region=(615, 365, 200, 150), confidence = 0.7)
    tresDois = auto.locateOnScreen("numero/3 2.png", region=(615, 365, 200, 150), confidence = 0.7)

    # quatro
    quatro = auto.locateOnScreen("numero/4.png", region=(615, 365, 200, 150), confidence = 0.7)
    quatroDois = auto.locateOnScreen("numero/4 2.png", region=(615, 365, 200, 150), confidence = 0.7)
    quatroTres = auto.locateOnScreen("numero/4 3.png", region=(615, 365, 200, 150), confidence = 0.7)

    # cinco
    cinco = auto.locateOnScreen("numero/5.png", region=(615, 365, 200, 150), confidence = 0.7)
    cincoDois = auto.locateOnScreen("numero/5 2.png", region=(615, 365, 200, 150), confidence = 0.7)
    cincoTres = auto.locateOnScreen("numero/5 3.png", region=(615, 365, 200, 150), confidence = 0.7)
    cincoQuatro = auto.locateOnScreen("numero/5 4.png", region=(615, 365, 200, 150), confidence = 0.7)

    # seis
    seis = auto.locateOnScreen("numero/6.png", region=(615, 365, 200, 150), confidence = 0.7)
    seisDois = auto.locateOnScreen("numero/6 2.png", region=(615, 365, 200, 150), confidence = 0.7)

    # sete
    sete = auto.locateOnScreen("numero/7.png", region=(615, 365, 200, 150), confidence = 0.7)
    seteDois = auto.locateOnScreen("numero/7 2.png", region=(615, 365, 200, 150), confidence = 0.7)

    # oito
    oito = auto.locateOnScreen("numero/8.png", region=(615, 365, 200, 150), confidence = 0.7)
    oitoDois = auto.locateOnScreen("numero/8 2.png", region=(615, 365, 200, 150), confidence = 0.7)
    oitoTres = auto.locateOnScreen("numero/8 3.png", region=(615, 365, 200, 150), confidence = 0.7)
    oitoQuatro = auto.locateOnScreen("numero/8 4.png", region=(615, 365, 200, 150), confidence = 0.7)

    # nove
    noveDois = auto.locateOnScreen("numero/9 2.png", region=(615, 365, 200, 150), confidence = 0.7)
    noveTres = auto.locateOnScreen("numero/9 3.png", region=(615, 365, 200, 150), confidence = 0.7)
    noveQuatro = auto.locateOnScreen("numero/9 4.png", region=(615, 365, 200, 150), confidence = 0.7)
    noveCinco = auto.locateOnScreen("numero/9 5.png", region=(615, 365, 200, 150), confidence = 0.7)

    if(zero or zeroDois):
        botao = auto.locateCenterOnScreen("numero/botao/zero.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(um or umDois or umDois):
        botao = auto.locateCenterOnScreen("numero/botao/um.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(dois or doisDois):
        botao = auto.locateCenterOnScreen("numero/botao/dois.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(tres or tresDois):
        botao = auto.locateCenterOnScreen("numero/botao/tres.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(quatro or quatroDois or quatroTres):
        botao = auto.locateCenterOnScreen("numero/botao/quatro.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(cinco or cincoDois or cincoTres or cincoQuatro):
        botao = auto.locateCenterOnScreen("numero/botao/cinco.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(seis or seisDois):
        botao = auto.locateCenterOnScreen("numero/botao/seis.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(sete or seteDois):
        botao = auto.locateCenterOnScreen("numero/botao/sete.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(oito or oitoDois or oitoTres or oitoQuatro):
        botao = auto.locateCenterOnScreen("numero/botao/oito.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)
    elif(noveDois or noveTres or noveQuatro or noveCinco):
        botao = auto.locateCenterOnScreen("numero/botao/nove.png", region=(615, 365, 200, 150), confidence = 0.9)
        if(botao):
            clicarBotao(botao)

            

#quantidade = 0
while (parar == True):
    if(key.is_pressed('8')):
        minerando = True
        while(minerando == True):
            for i in range(1, 6):
                minerio1 = auto.locateCenterOnScreen('minerio1.png', confidence = 0.9)
                minerio2 = auto.locateCenterOnScreen('minerio2.png', confidence = 0.9)
                minerio3 = auto.locateCenterOnScreen('minerio3.png', confidence = 0.9)
                if(minerio1):
                    x, y = minerio1
                    andar(x,y)
                elif(minerio2):
                    x, y = minerio2
                    andar(x,y)
                elif(minerio3):
                    x, y = minerio3
                    andar(x,y)
                    
                auto.moveTo(1,1)
                validacao = auto.locateOnScreen("numero/botao/enviar.png", region=(615, 365, 200, 150), confidence = 0.9)
                if(validacao):
                    validar()

                if(i == 1):
                    auto.moveTo(1383,129)
                    x = 1383
                    y = 129
                elif(i == 2):
                    auto.moveTo(1319,104)
                    x = 1319
                    y = 104
                elif(i == 3):
                    auto.moveTo(1282,108) 
                    x = 1282
                    y = 108
                elif(i == 4):
                    auto.moveTo(1308, 121)
                    x = 1308
                    y = 121
                elif(i == 5):
                    auto.moveTo(1335,174)
                    x = 1335
                    y = 174

                auto.mouseDown(button = 'left') # Clica no mapa para a prox localização
                auto.mouseUp(button = 'left')


                noLugar = True
                andando = True
                while(andando == True):
                    mapa = auto.screenshot("mapa1.png",region=(1260, 69, 120, 120))
                    #mapax, mapay = auto.locateCenterOnScreen("mapa1.png")
                    time.sleep(1)
                    #while(noLugar == True):
                    if((auto.locateCenterOnScreen("mapa1.png")) != None):

                        if(noLugar == True):
                            auto.keyDown('space')
                            auto.keyUp('space')
                            time.sleep(2)
                            auto.moveTo(x,y)
                            auto.mouseDown(button = 'left')
                            auto.mouseUp(button = 'left')
                        else:
                            andando = False
                        
                    else:
                        noLugar = False
                        time.sleep(1)




            if(key.is_pressed('0')):
                parar = False
        


