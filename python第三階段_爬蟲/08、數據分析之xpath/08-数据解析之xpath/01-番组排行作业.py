'''
    课后把这个番组计划爬10页 并且解析字段数据
        (如 标题，评分，评价数，排行，作者(class="info tip"的p下的内容))
    步骤
        1： https://bangumi.tv/book/browser?sort=rank&page=1 第一页
            https://bangumi.tv/book/browser?sort=rank&page=2   第二页
            https://bangumi.tv/book/browser?sort=rank&page=4 第四页
            get 目标url
            每一页 变化的地方就是page 经过分析 page的值就是页数 依次递增
        2：发起请求 获取每一页的响应
        3: 并且解析字段数据  BS4
            (如 标题，评分，评价数，排行，作者(class="info tip"的p下的内容))
'''
import requests
from bs4 import BeautifulSoup
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
for i in range(1, 2):
    url1 = f"https://bangumi.tv/book/browser?sort=rank&page={i}"
    # 推荐大家 解析写完 再去爬多页 先只爬一页 测试一下代码
    response = requests.get(url=url1, headers=headers1)  # 发起请求 获取每一页的响应
    response.encoding="utf-8"
    soup = BeautifulSoup(response.text,'html.parser')
    li_list=   soup.select('ul#browserItemList>li') # 每一条数据
    for li in li_list:
        # print(type(li))
        rank = li.select('span.rank')[0].text
        title = li.select_one('h3').text
        title1 = title.replace(' ','').replace('\n','')
        # info = li.select('div.inner>p')[0].text # 书籍信息
        info = li.select('p.info.tip')[0].text # 书籍信息 多个class值 如果当做条件 用. 别用空格
        info1=  info.replace(' ','').replace('\n','')
        fade = li.select('p.rateInfo>small')[0].text  # 评分
        tip_j = li.select('p.rateInfo>span.tip_j')[0].text  # 评分人数
        # print(fade,tip_j)
        print(rank,title1,info1,fade,tip_j)