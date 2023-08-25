import pyautogui as gui 
import time 
def openVS():
    gui.hotkey('win')
    time.sleep(.1)
    gui.write('vs code')
    gui.hotkey('enter')
    time.sleep(1)

def erase (): #this functuion to make sure that the search bar is empty
        with gui.hold('backspace'):
             gui.sleep(2)

def search (appName):
       time.sleep(1)
       gui.hotkey('ctrl','shift','x')
       time.sleep(1)
       erase()
       gui.write(appName)
       time.sleep(5)

def install ():
      gui.click('install1.png')