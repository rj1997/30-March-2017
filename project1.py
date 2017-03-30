"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome("C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser=webdriver.Chrome("D:\\New folder\\chromedriver_win32\\chromedriver.exe")
str="https://www.wikiwand.com/en/Mahatma_Gandhi"
browser.get(str)
import requests
res=requests.get(str)
file=open("C:\\Users\\Rishabh Jain\\Desktop\\Amazing.txt.txt","w")
file.write(res.text)
file=open("C:\\Users\\Rishabh Jain\\Desktop\\Amazing.txt.txt","r+")

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

"""
