"""
1: 练习一下百度这个网站的请求
    把这个响应的内容（网页的内容） 保存到html的文件
2：新浪首页 https://www.sina.com.cn/ 整个页面的内容 保存到html的文件
    提示 文件操作 with open 或者open方法 选其一
"""

import  requests

url1="https://www.sina.com.cn/"

headers = {
 #   'Accept': '*/*',
 #    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
 #    'Connection': 'keep-alive',
 #    'Content-type': 'application/x-www-form-urlencoded',
 #    'Origin': 'https://www.sina.com.cn',
 #    'Referer': 'https://www.sina.com.cn/',
 #    'Sec-Fetch-Dest': 'empty',
 #    'Sec-Fetch-Mode': 'cors',
 #    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    # 'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

response=requests.get(url=url1 ,headers=headers)
response.encoding="utf-8"
# print(response)

with open("02.html","w",encoding="utf-8") as f:
    f.write(response.text)

