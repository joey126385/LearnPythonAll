'''
    # https://httpbin.org/get

'''


import requests
proxies1 = {
    # 代理Ip
    # 注意 key的值 看协议的类型  值就写代理IP的值  格式 http://ip:port
    "https":"http://14.117.217.141:3828"
}
# proxies代理Ip
response = requests.get(url="https://httpbin.org/get",proxies=proxies1)
print(response.text)