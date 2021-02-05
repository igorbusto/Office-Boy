            
import pyautogui as auto
import keyboard as key
import time
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\Programas\pytesseract\tesseract.exe'
from PIL import Image
            
            
            
def clicarBotao(botao):
    x,y = botao
    auto.moveTo(x,y)
    auto.mouseDown(button = 'left')
    auto.mouseUp(button = 'left')

    enviar = auto.locateCenterOnScreen("numero/botao/enviar.png", region=(615, 365, 200, 150), confidence = 0.9)
    if(enviar):
        x,y = enviar
        auto.moveTo(x,y)
        sleep(1)
        auto.mouseDown(button = 'left')
        auto.mouseUp(button = 'left')

quantidade = 0
parar = True
while (parar == True):

    validacao = auto.locateOnScreen("numero/botao/enviar.png", region=(615, 365, 200, 150), confidence = 0.9)
    
    validado = False
    #if(key.is_pressed('+')):
    if(validacao):
        auto.moveTo(1,1)
        quantidade += 1
        print(quantidade)
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
                validado = True
        elif(um or umDois or umDois):
            botao = auto.locateCenterOnScreen("numero/botao/um.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(dois or doisDois):
            botao = auto.locateCenterOnScreen("numero/botao/dois.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(tres or tresDois):
            botao = auto.locateCenterOnScreen("numero/botao/tres.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(quatro or quatroDois or quatroTres):
            botao = auto.locateCenterOnScreen("numero/botao/quatro.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(cinco or cincoDois or cincoTres or cincoQuatro):
            botao = auto.locateCenterOnScreen("numero/botao/cinco.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(seis or seisDois):
            botao = auto.locateCenterOnScreen("numero/botao/seis.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(sete or seteDois):
            botao = auto.locateCenterOnScreen("numero/botao/sete.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(oito or oitoDois or oitoTres or oitoQuatro):
            botao = auto.locateCenterOnScreen("numero/botao/oito.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True
        elif(noveDois or noveTres or noveQuatro or noveCinco):
            botao = auto.locateCenterOnScreen("numero/botao/nove.png", region=(615, 365, 200, 150), confidence = 0.9)
            if(botao):
                clicarBotao(botao)
                validado = True

        if(validado == True):
            time.sleep(2)
            auto.moveTo(883,440)
            auto.mouseDown(button = 'left')
            auto.mouseUp(button = 'left')
            time.sleep(1)
            auto.moveTo(622,440)
            auto.mouseDown(button = 'left')
            auto.mouseUp(button = 'left')
            time.sleep(1)
            auto.moveTo(740,497)
            auto.mouseDown(button = 'right')
            auto.mouseUp(button = 'right')
            validado = False