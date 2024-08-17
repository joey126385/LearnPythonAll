import  re


def B_01_01():
    str1 = '<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索"  title="百度搜索2" />'

    # 貪婪模式
    # ['title="百度搜索"  title="百度搜索2"']
    print(re.findall('title=".*"', str1))

    # 非貪婪模式
    # ['title="百度搜索"', 'title="百度搜索2"']
    print(re.findall('title=".*?"', str1))

    # **   ()  回傳括號內的內容  回傳 list列表
    # ['百度搜索', '百度搜索2']
    print(re.findall('title="(.*?)"', str1))

def B_01_02():
    str2 = "aasdhj啊。是a123+多久啊开始123啊但是扩a大阿萨的b牛仔裤超牛卡21312"
    #    拿到了中文 返回了列表
    result = re.findall("[\u4e00-\u9fa5]", str2)
    print(result)

    # 使用列表拼接
    print("".join(result))

def B_01_03():
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
    print(re.findall('<div>(.*?)</div>', str1))# []
    print(re.findall('<div>(.*?)</div>', str1, re.S))
B_01_01()
B_01_02()
B_01_03()
