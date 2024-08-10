from bs4 import BeautifulSoup

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
<p>story</P>
"""
# pip install beautifulSoup4
soup = BeautifulSoup(html, 'html.parser')  # 实例化 直接把我们要解析的数据传进去
# print(soup)
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.p)  # 点标签名就可以拿到 只能拿第一个
print(soup.a)
print(soup.a['href'])  # 获取属性
soup.a['href'] = "www.baidu.com"  # 修改属性
print(soup.a.attrs)  # 拿到所有的属性
print(soup.a['id'])
print(soup.a.text) # 拿到所有的内容
print(soup.a.get_text()) # 拿到所有的内容
# string得到标签下的文本内容，只有在此标签下 没有子标签，
# 或者只有一个子标签的情况下才能
# 返回其中的内容，否则返回的是None;
print(soup.a.string)
#<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span>南风好帅</a>

