from time import sleep
import pyautogui as auto
import keyboard as key

parar = True
continuar = False

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

    

    #vida = auto.screenshot("medico/vidaTela.png",region=(684, 359, 62, 5))
    #mana = auto.screenshot("medico/manaTela.png",region=(684, 365, 62, 5))
    
    if(continuar == True):
        velocidade = auto.locateCenterOnScreen('buffs/velocidade.png', confidence = 0.9)
        ira = auto.locateCenterOnScreen('buffs/ira.png', confidence = 0.9)
        vampirismo = auto.locateCenterOnScreen('buffs/vampirismo.png', confidence = 0.9)

        if(ira == None):
            auto.keyDown('f5')
            auto.keyUp('f5')

        if(vampirismo == None):
            auto.keyDown('f6')
            auto.keyUp('f6')

        if(velocidade == None):
            auto.keyDown('v')
            auto.keyUp('v')

    if(key.is_pressed('+')):
        continuar = True
        print('continuou')

    if(key.is_pressed('-')):
        continuar = False
        print('parou')

    '''
    if(key.is_pressed('f9')):
        auto.keyDown(',')
        auto.keyUp(',')
        auto.keyDown('.')
        auto.keyUp('.')
        auto.keyDown(';')
        auto.keyUp(';')
        auto.keyDown('/')
        auto.keyUp('/')
        auto.keyDown(']')
        auto.keyUp(']')

    
    if(key.is_pressed('f10')):
    auto.keyDown('[')
    auto.keyUp('[')
    auto.keyDown(']')
    auto.keyUp(']')
    auto.keyDown('´')
    auto.keyUp('´')
    auto.keyDown('~')
    auto.keyUp('~')
    auto.keyDown('/')
    auto.keyUp(';')
    '''
