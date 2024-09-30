import pyautogui
import time
import random
import webbrowser

def mouse_jiggler(duration=5):
    screenWidth, screenHeight = pyautogui.size()
    while True:
        pyautogui.moveTo(random.randint(0, screenWidth), random.randint(0, screenHeight), duration)
        time.sleep(2)

def auto_clicker():
    while 1 > 0:
        pyautogui.click()
        time.sleep(1)

def autoReactionTime():
    webbrowser.open('https://humanbenchmark.com/tests/reactiontime')
    pyautogui.moveTo(1268, 634, 1)
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

def teleport():
    x, y = pyautogui.size()
    print(pyautogui.position())






if __name__ == "__main__":
    #mouse_jiggler(duration)
    #auto_clicker()
    #autoReactionTime()
    teleport()


