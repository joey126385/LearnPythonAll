'''
    我们是怎么提取代理IP的？
    我们访问 http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=83353&vkey=9EDD074B383437976F9A70B2F0E751D7&num=1&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1
    就会给我们返回一个IP
    可以用代码去请求这个链接 直接就可以拿到这个IP

'''

import requests
ip_url = "http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=83353&vkey=9EDD074B383437976F9A70B2F0E751D7&num=1&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1"
ip_res = requests.get(url=ip_url) # 请求ipurl 拿到代理IP的值
print(ip_res.text)
print('======')
url1 = "https://httpbin.org/get"
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
proxies1={
    # # 注意 key的值 看url协议的类型  value 值就写代理IP的值  格式 http://ip:port
    # "https":"http://117.27.108.196:3828"
    "https":f"http://{ip_res.text}" # 不能直接写死 每次请求 ip的值不一样
}
response = requests.get(url=url1,headers=headers1,proxies=proxies1)
print(response.text)