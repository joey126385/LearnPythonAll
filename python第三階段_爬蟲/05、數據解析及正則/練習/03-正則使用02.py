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
import re
print(re.findall('<p>(.*?)</p>', str1))
# 開始結束 不同行 需要使用 re.S 因為有 \n 換行
print(re.findall('<div>(.*?)</div>', str1)) #  []
print(re.findall('<div>(.*?)</div>', str1,re.S)) #  []