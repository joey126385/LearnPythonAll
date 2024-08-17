'''
    需求
        爬取斗鱼 主机游戏分类下的主播字段
    实现
        1：目标url
            https://www.douyu.com/g_TVgame get方式
            有我们要的数据
        2： 发起请求获取响应
        3：提取出我们要的内容
            正则提取
            提取出所有的主播字段
            所有的主播字典 "nn": "主播名字"
        拓展
            现在是三个列表保存了所有的数据
            有没有办法一一对应
            1个主播名字对应标题对应热度
'''
import  requests
import re
from fake_useragent import UserAgent
ua = UserAgent()
user_agent=ua.random
headers1 = {'user-agent': user_agent}
url1="https://www.douyu.com/g_TVgame"

response=requests.get(url=url1,headers=headers1)
# print(response.text)
# "rn": "电子榨菜来啦！！ 6696"
rn=re.findall('"rn":"(.*?)"',response.text)
print(len(rn))
