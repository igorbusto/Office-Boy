import pyautogui as auto
import keyboard as key
import time
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\Programas\pytesseract\tesseract.exe'
from PIL import Image


parar = True
while (parar == True):
    if(key.is_pressed('alt')):
        seis = auto.locateCenterOnScreen('numero/seis.png', confidence = 0.7)
        if(seis):
            x,y = seis
            #auto.moveTo(x,y)
            #print('entro')
            botaoSeis = auto.locateCenterOnScreen('numero/botao/botao seis.png', confidence = 0.9)
            if(botaoSeis):
                x,y = botaoSeis
                auto.moveTo(x,y)
                auto.mouseDown(button = 'left')
                auto.mouseUp(button = 'left')


        