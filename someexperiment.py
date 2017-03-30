from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
browser=webdriver.Chrome("C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe")
str="http://www.facebook.com"
browser.get(str)
pemail="rishabhjaingenius@gmail.com"
ppassword="Rj@241008"
aditya=browser.find_element_by_id('email')
aditya.send_keys(pemail)
aditya=browser.find_element_by_id('pass')
aditya.send_keys(ppassword)
aditya=browser.find_element_by_id('u_0_q')
aditya.click()