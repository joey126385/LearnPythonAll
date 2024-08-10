"""
作业
    爬取链接100页租房字段 租房的字段也要解析
    https://cs.lianjia.com/zufang/
"""
import requests
from lxml import etree
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
for page in range(1, 101):
    response = requests.get(url=f"https://cs.lianjia.com/zufang/pg{page}/#contentList", headers=headers1)
    tree = etree.HTML(response.text)
    data_list = tree.xpath('//div//div[@class="content__list--item--main"]')
    firstData = tree.xpath('//div[@class="content__list--item"]//div[1]//text()')

    # 去空白
def xpathFormat(xpath):
    text = data.xpath(xpath)
    result = "".join(text).strip().replace(' ', '').replace('\n', '').replace('\xa0', '')
    return result

print(len(data_list))
for data in data_list:
    print("標題", xpathFormat('.//p[@class="content__list--item--title"]//text()'))
    print("描述", xpathFormat('.//p[@class="content__list--item--des"]//text()'))
    print("看房", xpathFormat('.//p[@class="content__list--item--bottom oneline"]//text()'))
    print("更新", xpathFormat('.//p[@class="content__list--item--brand oneline"]//text()'))
    print("價格", xpathFormat('.//span[@class="content__list--item-price"]//text()'))
    print(f"--------{page}-----------------\n")
