#To play 2048 game.. Brute Force logic used
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui,time
browser=webdriver.Chrome("C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe")
str="http://2048game.com/"
browser.get(str)
for i in range(50):
    pyautogui.press('left')
    time.sleep(0.25)
    pyautogui.press('up')
    time.sleep(0.25)
    pyautogui.press('right')
    time.sleep(0.25)
    pyautogui.press('down')
    time.sleep(0.25)

