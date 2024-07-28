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
import re

import requests

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
url1 = "https://www.douyu.com/g_TVgame"
response = requests.get(url=url1, headers=headers1)
# print(response.text) # 确定了 我们拿到了目标的数据

# "nn": "王拉奇" 页面格式化以后 有空格 未格式化没有空格 "nn":"王拉奇"
# 我们拿到的响应 没有空格！！！ 以文本的响应为准
nn_name = re.findall('"nn":"(.*?)"', response.text)  # 写规则匹配 响应的内容 取出我们符合规则的数据
# "ol":2673851,
ol_list = re.findall('"ol":(.*?),', response.text)
# "rn":"阿飞）不稳定世1魔剑",
rn_list = re.findall('"rn":"(.*?)",', response.text)
print(nn_name, ol_list, rn_list)
print(len(nn_name), len(ol_list), len(rn_list))
for i in range(0, len(rn_list)):  # 循环遍历列表长度
    print(nn_name[i] + "====", rn_list[i] + "====", ol_list[i])
    # 索引取值 把三个字段一一对应
    # 循环第一次 拿列表第一个元素 循环第二次拿第二个
