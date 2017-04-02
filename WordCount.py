import requests
res=requests.get('https://en.wikipedia.org/wiki/Gwalior')
str=res.text
import bs4
soup=bs4.BeautifulSoup(str,'lxml')
#print(soup.prettify())

[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
#print(visible_text)


def count_words(line):
    words={}
    for w in line.split():
        words[w]=words.get(w,0)+1
    for w,c in words.items():
        print(w,c)
count_words(visible_text)
