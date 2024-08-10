import re
str1 = "女孩 天使 羽毛\ 翅/膀 4 *K?动:漫壁纸38402160.jpg.jpg"
# 替换的方法 参数1 规则 匹配什么数据 参数2 替换成啥 参数3 对哪个字符串做处理
# result =  re.sub('[\\s\\\\/:\\*\\?\\\"<>\\|]','',str1)
result =  re.sub('[\\\\/:*?\"<>|]','',str1)
# python的replace替换 也可以处理文件名非法字符
print(result)