'''
        需求
            爬取番组计划的图书信息
        分析步骤
            1： 明确目标url
                找一下图书的信息在哪个链接里有
                https://bangumi.tv/book/browser?sort=rank&page=1 get请求
            2：发起请求  获取响应
            3： 从响应的内容 取出图书信息的字段
                html数据的解析  bs4

                找到每一条数据他是被谁包裹的 写规则定位到这个标签
                    每一条数据 都是在li 里面
                    写一个规则 匹配到所有数据的li 就可以循环解析每一条数据了
                    ul#browserItemList>li
'''

import requests
from bs4 import BeautifulSoup
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
url1 = "https://bangumi.tv/book/browser?sort=rank&page=1"

response = requests.get(url=url1, headers=headers1)
# <meta charset="utf-8" />
response.encoding = "utf-8"
# print(response.text)  # 发起请求  获取响应
#  3： 从响应的内容 取出图书信息的字段

soup = BeautifulSoup(response.text, 'html.parser')
li_list = soup.select('ul#browserItemList>li') # 用css选择器拿到所有图片数据所在的li

for li in li_list:  # 循环取出每一个li的数据
    # print(li) # 第一次循环就是第一条数据
    title = li.select('div.inner>h3')[0].text  # 列表索引取值 取出元素再获取内容
    title1 = title.replace('\n', '')  # 替换换行为空
    print(title1)
    print('===============')
