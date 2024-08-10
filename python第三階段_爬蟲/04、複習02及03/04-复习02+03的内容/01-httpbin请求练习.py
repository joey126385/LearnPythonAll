'''
        requests 可以帮我们发起请求
        如何发起get请求
            https://httpbin.org/get
            确定目标url 看他的请求方式
        https://cn.bing.com/images/search?q=小姐姐照片&form=HDRSC2&first=1
        问号前面的是路由(路径) 后面的是参数
        参数一般是键值对格式 key=value 多个参数&链接

        https://httpbin.org/get?name=nanfeng
'''

import requests

url1 = "https://httpbin.org/get"
headers1 = {
    # "Accept-Language": "zh-CN,zh;q=0.9", # 演示一下
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# response = requests.get(url=url1,headers=headers1)  # 请求哪个url 就放哪个url

url2 = "https://httpbin.org/get?name=nanfeng"
# get请求的参数传递 方法1 直接写在地址栏
# response = requests.get(url=url2, headers=headers1)  # 练习get请求传参 方法1
#  get请求的参数传递 方法2 params 值是字典类型的
params1 = {
    "age": 18
} # 这个是requests给我们提供的传参方法
response = requests.get(url=url2, headers=headers1,params=params1)
# 现在 我们是测试网站 参数我们随便写 如果是实战爬取呢？
# 不能了 人家传什么参数 我们就要传啥 真人传了name=nanfeng  你如果随便去写 name1=123 和真人不一样 可能会访问失败
#！！！！！ 所以我们看人家传了啥参数 我就去传对应的！！！！！



print(response)  # <Response [200]>

print(response.text)  # 拿响应的内容 字符串返回
