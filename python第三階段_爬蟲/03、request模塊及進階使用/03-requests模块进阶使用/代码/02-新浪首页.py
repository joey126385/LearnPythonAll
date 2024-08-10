'''
        新浪首页 https://www.sina.com.cn/ 整个页面的内容 保存到html的文件
        步骤
            1： 找到目标url
                https://www.sina.com.cn/ get请求
            2：发起请求 获取响应
            3： 保存到本地html文件
'''
import requests

headers1 = {
    # 复制真人身份
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get("https://www.sina.com.cn/",headers=headers1)
response.encoding="utf-8"
print(response.text) # 请求成功了
'''
    f = open("sina.html","w",encoding="utf-8")
    f.write(response.text) # 响应的内容（网页的内容）
    f.close()

'''
# 第二个
with open("sina.html","w",encoding="utf-8")as f:
    f.write(response.text)
