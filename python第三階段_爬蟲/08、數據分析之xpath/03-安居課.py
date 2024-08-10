import requests
from lxml import etree

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
response = requests.get(url="https://cs.zu.anjuke.com/?from=HomePage_TopBar", headers=headers1)
tree = etree.HTML(response.text)

"""
標題
"""
m=tree.xpath('//div[@class="zu-itemmod clearfix"]') # 35

def xpathData(xpath):
    text = data.xpath(xpath)
    result = "".join(text).strip().replace(' ', '').replace('\n', '').replace('\xa0', '')
    return result

for data in m:
    print("标题", xpathData('.//div[@class="zu-info"]//h3//a//text()'))
    print("房屋详情", xpathData('.//div[@class="zu-info"]//p[@class="details-item tag"]//text()'))
    print("房屋标签", xpathData('.//div[@class="zu-info"]//p[@class="details-item bot-tag"]//text()'))
    print("房屋地址", xpathData('.//div[@class="zu-info"]//address[@class="details-item tag"]//text()'))
    print("價格",xpathData('.//div[@class="zu-side"]//text()'))
    print("--------------------")

