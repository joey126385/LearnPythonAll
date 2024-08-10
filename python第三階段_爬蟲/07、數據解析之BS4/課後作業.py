"""
课后把这个番组计划爬10页 并且解析字段数据(如
标题，
评分，
评价数，
排行，
作者(class="info tip"的p下的内容))
"""
import requests
from bs4 import BeautifulSoup
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
for page in range(1,2):
    url1 = f"https://bangumi.tv/book/browser?sort=rank&page={page}"
    response = requests.get(url=url1, headers=headers1)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.select('ul#browserItemList>li>div.inner')# 24
    # print(len(result))
    for data in result:
        print("标题",data.select('h3>a')[0].text)
        print("评分", data.select('p.rateInfo>small')[0].text)
        print("评价数", data.select('p.rateInfo>span.tip_j')[0].text)
        print("排行", data.select('span')[0].text)
        print("作者", data.select('p.info')[0].text.split())
        print("----------")
"""
    <div class="inner">
        <h3><a class="l" href="/subject/18462">灌篮高手 完全版</a> <small class="grey">SLAM DUNK 完全版</small></h3>
        <span class="rank"><small>Rank </small>1</span>
        <p class="info tip">
            276话 / 2001-03-19 / 井上雄彦 / 集英社
        </p>
        <p class="rateInfo">
            <span class="starstop-s"><span class="starlight stars9"></span>
            </span> 
            <small class="fade">9.4</small> 
            <span class="tip_j">(1543人评分)</span>
        </p>
    </div>
"""