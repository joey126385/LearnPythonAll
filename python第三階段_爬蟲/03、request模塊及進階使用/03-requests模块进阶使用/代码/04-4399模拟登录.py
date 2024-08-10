'''
    需求
        爬取4399群组页面的数据
    1：找目标url
        https://my.4399.com/forums/index-getMtags?type=game
        get请求
    2： 发起 请求 获取响应

    模拟登录
        1： 找到登录接口
            https://ptlogin.4399.com/ptlogin/login.do?v=1 ?前面是路径 问号后面是参数
            post 请求
            password: nanfeng
            username: 15348438633
            post请求传参
            data 实现的 类型也是字典
        2: 请求登录接口 发送账号密码
            发正确的账号密码


'''

import requests

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
data1 = {
    "password": "nanfeng",
    "username": "15348438633"
}
login = requests.post(url="https://ptlogin.4399.com/ptlogin/login.do?v=1", headers=headers1, data=data1)
print(login.cookies) # 打印cookie信息 RequestsCookieJar对象
print(requests.utils.dict_from_cookiejar(login.cookies))
# response = requests.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1)
# response.encoding = "utf-8"
# print(response.text)  # 爬取失败 # 代码他现在知道我们登陆了吗？不知道 访问页面 默认是没有的登录的
# 我们需要告诉他 我们现在的状态是 登录了的状态

response = requests.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1,cookies= login.cookies) # 带上登录后的cookie
response.encoding = "utf-8"
# print(response.text) # 登录成功后的值