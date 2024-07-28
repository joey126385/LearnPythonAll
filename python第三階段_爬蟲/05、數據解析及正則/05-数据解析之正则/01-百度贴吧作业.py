'''
    爬取五个贴吧的内容(只要爬1页)保存到本地html
    需求
        爬取百度贴吧的内容保存到本地html
    实现
        1：确定目标url
            我们要的内容 在互联网的位置
            https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80 get请求
            url里面有中文 传输的时候会编码 url编码
            %E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80 = 王者荣耀  对我们去发起请求 没有太大影响
        2：发起请求 获取响应
            页面的数据是会更新的 注意！！！
        3： 保存到本地html
            确定文件有我们要的数据就行
        kw 的值就是对应的贴吧名字
        分析发现 不同的贴吧url 只是kw的值不一样

'''
import requests

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
# 方法1
# kw = input('请输入贴吧名字：') # 用户输入哪个列表爬哪个贴吧
# response = requests.get(url=url1, headers=headers1)  # 拿到了我们要的数据
# # print(response.text)
#
# f = open(f'{kw}.html', 'w', encoding="utf-8")
# f.write(response.text)
# f.close()
# 方法2
kw = ["抗压吧", "DNF", "逆水寒", "魔兽世界", "永劫无间"]  # 定义了一个列表 存储了五个贴吧
for i in kw:
    print(i) # 循环依次请求每一个 循环依次 i==kw的值 就会不一样
    url1 = f"https://tieba.baidu.com/f?kw={i}"  # f插值法 请求 用户输入的贴吧
    response = requests.get(url=url1, headers=headers1)  # 拿到了我们要的数据
    # print(response.text)

    f = open(f'{i}.html', 'w', encoding="utf-8")
    f.write(response.text)
    f.close()
    print(f"当前{i}贴吧内容保存成功")