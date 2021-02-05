import pyautogui as auto
import keyboard as key
import time
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\Programas\pytesseract\tesseract.exe'


parar = True
while (parar == True):
    vidaFull = auto.locateOnScreen("medico/vidaFull.png", region = (684, 359, 62, 5))
    if(vidaFull == None):
        vida2 = auto.locateOnScreen("medico/vida2.png", region = (684, 359, 62, 5), confidence = 0.9)
        vida1 = auto.locateOnScreen("medico/vida1.png", region = (684, 359, 62, 5), confidence = 0.9)
        if(vida2):
            auto.keyDown('f1')
            auto.keyUp('f1')
            auto.keyDown('q')
            auto.keyUp('q')
        if(vida1):
            auto.keyDown('q')
            auto.keyUp('q')

    manaFull = auto.locateOnScreen("medico/manaFull.png", region=(684, 365, 62, 5))
    if(manaFull == None):
        mana = auto.locateOnScreen("medico/vida2.png", region=(684, 365, 62, 5), confidence = 0.9)
        if(mana):
            auto.keyDown('f3')
            auto.keyUp('f3')
            

