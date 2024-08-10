import requests
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

image_url = "https://q7.itc.cn/q_70/images03/20240718/f42231aa67084d7cb572fc938301af75.jpeg"
# 图片的格式 后缀 jpg png jpeg
# 保存图片 是要把图片的响应的数据拿到 也就是拿到这个链接对应的二进制数据
response =  requests.get(url=image_url,headers=headers1)
# response.content 获取字节数据 二进制返回
# print(response.content)
# print(response.text)
# 二进制是 要wb写入
with open("南风.jpeg",'wb')as f:
    f.write(response.content)