import pyautogui as auto
import keyboard as key
import time
import pytesseract
from PIL import Image

parar = True

while (parar == True):

    if(key.is_pressed('8')):
        #auto.dragTo(890, 523, button='left')
        
        x = 890
        y = 523

        auto.moveTo(x,y-70) #cima
        auto.dragTo(x, y,0.2, button='left')

        '''auto.moveTo(x+90,y-70) #direita cima
        auto.drag(890, 523, button='left')

        auto.moveTo(x+90,y) #direita
        auto.drag(890, 523, button='left')

        auto.moveTo(x+90,y+70) #direita baixo
        auto.dragTo(890, 523, button='left')

        auto.moveTo(x,y+70) #baixo
        auto.dragTo(890, 523, button='left')

        auto.moveTo(x-70,y+70) #esquerda baixo
        auto.dragTo(890, 523, button='left')

        auto.moveTo(x-70,y) #esquerda
        auto.dragTo(890, 523, button='left')

        auto.moveTo(x-70,y-70) #esquerda cima
        auto.dragTo(890, 523, button='left')'''
      

    if(key.is_pressed('7')):

        #auto.moveTo(890,523)#centro
        x = 890
        y = 523
        auto.moveTo(x,y-70) #cima
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x+90,y-70) #direita cima
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x+90,y) #direita
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x+90,y+70) #direita baixo
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x,y+70) #baixo
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x-70,y+70) #esquerda baixo
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')
        
        auto.moveTo(x-70,y) #esquerda
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')

        auto.moveTo(x-70,y-70) #esquerda cima
        auto.mouseDown(button = 'left')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'left')


      
                
        

        '''# Cima
        auto.moveTo(x=747, y=372)
        loot()
        auto.moveTo(810, 373)
        loot()
        auto.moveTo(803, 439)
        loot()
        auto.moveTo(807, 502)
        loot()
        auto.moveTo(746, 503)
        loot()
        auto.moveTo(682, 489)
        loot()
        auto.moveTo(682, 450)
        loot()
        auto.moveTo(683, 375)
        loot()'''



    if(key.is_pressed('1')):
        #print(auto.position())
        

        

    if(key.is_pressed('0')):
        parar = False


def loot():
        #auto.keyDown('shift')
        auto.mouseDown(button = 'right')
        auto.moveTo(890,523)
        auto.mouseUp(button = 'right')
        #auto.keyUp('shift')

