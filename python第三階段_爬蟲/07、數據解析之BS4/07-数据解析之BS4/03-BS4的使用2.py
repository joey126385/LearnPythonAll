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

soup = BeautifulSoup(html, 'html.parser')  # 实例化 直接把我们要解析的数据传进去

# print(soup.find_all('a')) # 查找所有符合条件的标签 返回列表
# print(len(soup.find_all('p'))) # 查找所有符合条件的标签 返回列表
#
# print(soup.find_all('p', class_="story"))  # class在python是关键字
# print(soup.find_all('a', id="link2"))
# print(soup.find_all('p', id="link2"))  # 匹配不到数据 没有这样的内容

#  重点 练习 css选择器的使用
# result = soup.select('p.story>a') # 写css选择器匹配到所有符合条件的 >子代
# result = soup.select('p.story a') # 写css选择器匹配到所有符合条件的 空格 后代
# result = soup.select('a#link2') #
# result = soup.select_one('a#link2') # select_one 匹配符合条件的第一个
result = soup.select_one('p.story a') # select_one 匹配符合条件的第一个
print(result)
