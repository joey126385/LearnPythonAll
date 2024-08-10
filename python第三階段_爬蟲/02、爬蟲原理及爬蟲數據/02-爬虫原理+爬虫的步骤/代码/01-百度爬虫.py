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
'''
import requests
headers1 = {
    # 复制真人身份
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# get这个方法可以帮我们发起一个get请求 传一个请求的url
response = requests.get(url="https://www.baidu.com/",headers=headers1)  # 发起请求 获取响应
# print(response)  # <Response [200]>
# 查看响应内容，response.text 字符串数据
# print(response.text)
# 查看响应头部字符编码 response.encoding
print(response.encoding)  # ISO-8859-1 响应的内容是这个编码 所以他就乱码了
response.encoding = "utf-8"
print(response.text)
# 查看响应头 response.headers
# print(response.headers)
# 查看请求头 response.request.headers
print(response.request.headers)
# 'User-Agent': 'python-requests/2.31.0' # 爬虫的身份
# ua代表我们当前的身份 真人的身份是浏览器  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3
print(response.status_code)  # 打印状态码 200  返回了一个假的响应
# 用爬虫的身份去访问人家网站 他不给我们返回数据了
# 伪装 伪装成真人 因为真人访问没问题
# headers 去携带请求头信息 字典格式
headers1 = {
    # 复制真人身份
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# 爬虫拿的是页面最新的
