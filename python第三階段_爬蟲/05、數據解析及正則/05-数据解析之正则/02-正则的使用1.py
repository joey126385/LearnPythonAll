import re

str1 = '<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索"  title="百度搜索2" />'

# 需求 匹配 这个标题的属性值
# findall 查找所有匹配的结果 然后返回列表 没有匹配到返回空列表 参数1 正则规则 参数2 要在哪个字符串里面匹配
#  .*? 把我们要匹配的内容 换成 .*?
#  在python中 数量词默认是贪婪
# 贪婪模式匹配 在表达式匹配成功的前提下 尽可能多匹配 .*
# 非贪婪模式 在表达式匹配成功的前提下 尽可能少匹配 .*? 量词后面跟? 表示非贪婪匹配 尽可能的少的匹配
# result = re.findall('title=".*"', str1)  # 返回了几个数据？1个 贪婪模式
# result = re.findall('title=".*?"', str1)  # 返回了几个数据？2个 非贪婪
result = re.findall('title="(.*?)"', str1)  # () 返回括号的内容
print(result,len(result))

str2= "aasdhj啊。是a123+多久啊开始123啊但是扩a大阿萨的b牛仔裤超牛卡21312"
# 中文的Unicode的编码范围主要在[u4e00-u9fa5]
result = re.findall("[\u4e00-\u9fa5]", str2) # 拿到了中文 返回了列表
# list--->str
str_res = ''.join(result) # 拼接列表里的值 转成字符串
print(str_res)





