"""
"""

import requests
import re

str1 = '<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索"  title="百度搜索2" />'

str2= """ 
<html>
    <body>
    <p>python1</p>
    <p>python2</p>
    <p>python3</p>
    <p>python4</p>
    <div>
        Line 1
    </div>
    </body>
</html>
"""
str3= "aasdhj啊。是a123+多久啊开始123啊但是扩a大阿萨的b牛仔裤超牛卡21312"
def match():
    s="123AAAA"
    print(re.match('www', 'www.runoob.com').span())
    print(re.match('com', 'www.runoob.com'))
    print(re.match("1?",s))
    print(re.match("4?",s))

def ex01():

    result01 = re.findall('title=".*"', str1)



def ex02():
    str1 = """ 
    <html>
        <body>
        <p>python1</p>
        <p>python2</p>
        <p>python3</p>
        <p>python4</p>
        <div>
            Line 1
        </div>
        </body>
    </html>
    """

def main ():
    # ex01()
    match()

main ()