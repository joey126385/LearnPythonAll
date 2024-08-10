from bs4 import BeautifulSoup

# html 標籤
html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span>南风好帅</a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" aaa="abc" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<h1 class="story">...</h1>
<p>story</P>
"""

soup = BeautifulSoup(html, 'html.parser')
# print(soup.p) #獲取標籤 第一個內容
# print(soup.h1)
# print(soup.a)
# print(soup.a['href'])
# print(soup.a.text)
print(soup.find_all('a'),len(soup.find_all('a')))


