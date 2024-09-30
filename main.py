import pyautogui
import time
import random
import webbrowser

def mouse_jiggler(repetitions=5, duration = 2, delay = 2):
    screenWidth, screenHeight = pyautogui.size()
    while repetitions > 0:
        pyautogui.moveTo(random.randint(0, screenWidth), random.randint(0, screenHeight), duration)
        time.sleep(delay)
        repetitions -= 1

def auto_clicker(secondsBetweenClicks=1, repetitions=100, delay=5):
    time.sleep(delay)
    while repetitions > 0:
        pyautogui.click()
        time.sleep(secondsBetweenClicks)
        repetitions -= 1

def autoReactionTime(open=True, automatic=True):
    if open == True:
        webbrowser.open('https://humanbenchmark.com/tests/reactiontime')
    else:
        if automatic==True:
            pyautogui.moveTo(1268, 634, 1)
        else:
            time.sleep(3)
    for i in range(5):
        if pyautogui.pixelMatchesColor(1647, 410, (43,135,209)) == True:
            pyautogui.click()
            zmaga = False
            while zmaga == False:
                im1 = pyautogui.screenshot()
                if pyautogui.pixelMatchesColor(1647, 410, (206,38,54)):
                    pass
                else:
                    pyautogui.click()
                    zmaga = True

def teleport(n=5, checkTime=0.1):
    screenWidth, screenHeight = pyautogui.size()
    while True:
        x, y = pyautogui.position()
        if x == 0:
            pyautogui.moveTo(screenWidth, y)
            n-=1
        elif x == screenWidth-1:
            pyautogui.moveTo(0, y)
            n-=1
        
        time.sleep(checkTime)

def forms(message="hello"):
    #https://docs.google.com/forms/u/0/d/e/1FAIpQLScXcP5bhsp-VyiT1gxxBerm9zZ1ZBvuFqASZ-eDYQTXZh_vjg/formResponse
    time.sleep(2)
    pyautogui.press(['tab', 'tab', 'tab', 'tab'])
    #1
    pyautogui.press('up')
    time.sleep(1)
    '''
    pyautogui.press('up')
    pyautogui.press('up')
    time.sleep(1)'''
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(1)
    a = [x for x in message]
    pyautogui.press(a)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('up')
    time.sleep(1)
    ''''
    pyautogui.press('up')
    pyautogui.press('up')
    time.sleep(1)'''
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    








if __name__ == "__main__":
    #mouse_jiggler()
    #auto_clicker()
    #autoReactionTime()
    #teleport()
    forms()


