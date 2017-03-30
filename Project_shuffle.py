import requests
import webbrowser
import os
#webbrowser.open('http://www.quora.com')
r = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(r.status_code)
print(r.status_code == requests.codes.ok)
r.raise_for_status()
print(r.text[0:250])

#text_file = open('C:\\Users\\Rishabh Jain\\Desktop\\writable.txt','wb')
#for chunk in r.iter_content(100000):
   # text_file.write()

