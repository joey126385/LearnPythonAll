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
# Line 1 #，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始
print(re.findall('<div>(.*?)</div>', str1)) #  []
# 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配
print(re.findall('<div>(.*?)</div>', str1,re.S))