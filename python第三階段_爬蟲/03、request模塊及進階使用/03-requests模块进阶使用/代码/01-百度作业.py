'''
        需求
            我们需要爬取百度首页的内容
        不管爬啥网站 跟着爬虫四步走
        1： 明确目标url
            确定一下 我们要的内容 在互联网上的位置 (url地址)
            https://www.baidu.com/  里面有我们要的内容
            get请求 请求url  https://www.baidu.com/ 请求头。。。。
        2：爬取 发起请求 获取响应
            python 没有自己实现http请求
            requests 请求测试的模块 可以帮我们发起http请求 需要下载 pip install requests
            代码发起请求
                看目标url的信息

            # 响应是人家给我们的 请求是我们自己去发起的
        把这个响应的内容（网页的内容） 保存到html的文件
'''

import requests
headers1 = {
    # 复制真人身份
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url="https://www.baidu.com/",headers=headers1)
response.encoding = "utf-8"  # 看响应的内容的 head里的meta标签的charset的值 是啥我们填啥

print(response.text)  # 打印响应的内容 字符串返回
# 查看请求头 response.request.headers
print(response.request.headers)

# 把这个响应的内容（网页的内容） 保存到html的文件 txt jpg
# 如果是图片 二进制数据
f = open("baidu.html","w",encoding="utf-8")
f.write(response.text) # 响应的内容（网页的内容）
f.close()