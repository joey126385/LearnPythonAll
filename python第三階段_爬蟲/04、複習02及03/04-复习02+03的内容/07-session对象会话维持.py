'''
    说白了就是比如你使用session成功的登录了某
    个网站，则在再次使用该session对象请求该网站
    的其他网页都会默认使用这个session
    之前使用的cookie等参数
    requests.session() 会话保持
    如果你用如果session登录了某个网站 就会一直保持
    实例化之后所有的请求都使用 不使用他请求 就维持不了会话
    用法：
         session1= requests.session() 实例化
         后面每次发get/post请求 用session1.get()
'''

import requests

session1 = requests.session()  # 加括号 实例化
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
data1 = {
    "password": "nanfeng",
    "username": "15348438633"
}
login_url = "https://ptlogin.4399.com/ptlogin/login.do?v=1"
login_res = session1.post(url=login_url, headers=headers1, data=data1)
# 怎么验证一下我们有没有成功呢？ 直接访问这个需要登录的网站 带上cookie看看能不能访问成功
# 能访问成功 我们就登录成功了 否则反之
print(login_res.cookies) # RequestsCookieJar
# 访问目标url 这个url的响应有我们要的数据
response = session1.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1) # 带上登录后的cookie session1自动带cookie
response.encoding = "utf-8"
print(response.text) # 登录成功后的值