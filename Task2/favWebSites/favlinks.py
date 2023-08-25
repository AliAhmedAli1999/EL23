import webbrowser as web
import pyautogui as gui 
import time
def firefox (site) :
    web.get('firefox').open_new_tab(site)
