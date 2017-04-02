from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path="C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe" #Path to chromedriver in memory
browser=webdriver.Chrome(path)
str="http://www.facebook.com"
browser.get(str)
email="abc@xyz.com" #Put your e-mail here
password="Password" #Put password to your facebook account here
field=browser.find_element_by_id('email')
field.send_keys(email)
field=browser.find_element_by_id('pass')
field.send_keys(password)
time.sleep(1)
button=browser.find_element_by_xpath('//*[@id="u_0_q"]')
button.click()
time.sleep(10)
drop=browser.find_element_by_xpath('//*[@id="userNavigationLabel"]')
drop.click()
browser.maximize_window()
time.sleep(300)
import pyautogui
#Subjective to where the logout button is on your screen
#Works fine for 1366x768 screen
pyautogui.moveTo(911,468,2.5)
pyautogui.click(911,468,1)
