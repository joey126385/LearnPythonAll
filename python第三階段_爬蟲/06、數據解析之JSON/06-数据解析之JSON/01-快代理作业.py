'''
    https://www.kuaidaili.com/free/
    用正则匹配这一页所有的 IP PORT 匿名度
    只要这三个 其他的不用做
    网站 获取匿名度的时候 他的代码固返回高匿名 我们可以固定写死
    实现思路
        1： 明确目标url
            确定IP port这些值 在哪个请求的响应
            https://www.kuaidaili.com/free/ get 请求
        2： 发起请求 获取响应
            用python代码 去拿到这个数据 页面内容数据(有我们要的字段)
        3：数据解析  用正则匹配
            从响应的内容里面 取出我们需要的字段
'''
import re

import requests

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
url1 = "https://www.kuaidaili.com/free/"
response = requests.get(url=url1, headers=headers1)  # 发起请求 获取响应
# print(response.text) # 确定一下 请求有没有 响应的内容 有我们要的数据
# 3：数据解析  用正则匹配
ip_list = re.findall('"ip": "(.*?)",', response.text)  # ip的值
port_list = re.findall('"port": "(.*?)"', response.text)  # port 的值
# print(len(ip_list))
# print(len(port_list))
a = "高匿名"
for i in range(0, len(ip_list)):
    print(ip_list[i], port_list[i], a)
