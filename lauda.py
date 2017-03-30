"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome("C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe")
str="https://www.google.co.in/search?q=greatest+person+on+earth&oq=greatest+person+on+earth&aqs=chrome..69i57j69i60l3.6226j0j7&sourceid=chrome&ie=UTF-8"
browser.get(str)
print(browser.page_source)
elems=browser.find_elements_by_class_name('r')
print("Length of elems is "+len(elems))
for i in range(len(elems)):
    print(elems[i])
    elems[i].click()"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome("C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe")
str="https://www.wikiwand.com/en/Mahatma_Gandhi"
browser.get(str)
import requests
res=requests.get(str)
file=open("C:\\Users\\Rishabh Jain\\Desktop\\Amazing.txt.txt","w")
file.write(res.text)

word_search=input("Enter the word to search : ")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1


for i,j in wordcount.items():
    if i==word_search:
     print(i,wordcount[i])

