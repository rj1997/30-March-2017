html_doc = """
<html><head><title>  <fcuk> The Dormouse's story </fcuk> </title></head>
<body>
<p class="title sponsor" class="bullshit" id="4"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,"lxml")
import re
for tag in soup.find_all(True):
   print(tag.name)



def not_lacie(href):
    return href and not re.compile(r'lacie').search(href)
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
print("Madbadhgsajhdhbdjsah")
print(soup.find_all(class_=has_six_characters))

