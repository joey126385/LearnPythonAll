'''
        post请求练习
        https://httpbin.org/post post请求的url
        浏览器直接访问 是发get请求 url是post请求的方法 方法不一致 会访问失败
        用代码访问就行了
'''
import requests

url1 = "https://httpbin.org/post"
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# 链接是post请求的方式  用post方法
# response = requests.post(url=url1,headers=headers1) # 发起请求
# post请求 传递参数用data ！！！！ 格式是字典键值对
data1 = {
    "name": "nanfeng"
}
'''
    post请求 参数一般放在请求体 参数不在url里面显示
    get请求  参数一般是url里面显示传递 
'''
response = requests.post(url=url1, headers=headers1, data=data1)
print(response.text) # 拿响应的内容 字符串的形式打印
