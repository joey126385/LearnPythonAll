'''
        模拟登录
        1： 找到登录接口 输入一个错误的账号密码 找url
            https://ptlogin.4399.com/ptlogin/login.do?v=1 ?前面是路径 问号后面是参数
            post 请求
            password: nanfeng
            username: 15348438633
            post请求传参
            data 实现的 类型也是字典
            人家网站怎么传的 我们也怎么传
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
login_url = "https://ptlogin.4399.com/ptlogin/login.do?v=1"
login_res = requests.post(url=login_url, headers=headers1, data=data1)
# 怎么验证一下我们有没有成功呢？ 直接访问这个需要登录的网站 带上cookie看看能不能访问成功
# 能访问成功 我们就登录成功了 否则反之
print(login_res.cookies) # RequestsCookieJar
# 访问目标url 这个url的响应有我们要的数据
response = requests.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1,cookies =login_res.cookies) # 带上登录后的cookie
response.encoding = "utf-8"
print(response.text) # 登录成功后的值
'''
    总结
        访问登录后的页面 有两种方法
        1： 手动复制登录后的cookie
            1.1 写在请求头
            1.2 cookies参数传递
        2：使用代码 模拟登录
            cookies参数传递
        推荐大家使用第一种(手动复制登录后的cookie) 第一种简单 
        用代码去模拟登录 难度较高 而且可能有加密 和验证码 
        他们都能实现我们要的效果 (爬取登录后才能看到的页面)
'''
