'''
    需求 爬取安居客长沙的租房信息数据 并取出租房字段
    步骤思路
        1：目标url
            https://cs.zu.anjuke.com/?from=HomePage_TopBar get请求
        2： 发请求 获取响应
        3： 数据解析
            xpath取出租房的数据
            先找每一条数据的位置 通过每一条数据 取出里面的租房字段
'''
import requests
from lxml import etree

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# 发起请求 获取响应
response = requests.get(url="https://cs.zu.anjuke.com/?from=HomePage_TopBar", headers=headers1)
# print(response.text)
tree = etree.HTML(response.text)

# xpath返回列表 没匹配到也会返回空列表
div_list = tree.xpath('//div[@class="zu-itemmod clearfix"]')
# print(div_list)
for div in div_list:  # 循环取出每一条数据
    # 模块源码的问题 局部遍历
    # title = div.xpath('//div[@class="zu-info"]/h3//b/text()')
    # 前面加个点 表示当前节点
    title = div.xpath('.//div[@class="zu-info"]/h3//b/text()')[0]  # 标题
    detail = div.xpath('.//div[@class="zu-info"]/p[@class="details-item tag"]//text()')  # 房屋详情
    label = div.xpath('.//div[@class="zu-info"]/p[@class="details-item bot-tag"]/span/text()')  # 房屋标签
    address = div.xpath('.//div[@class="zu-info"]/address[@class="details-item tag"]//text()')  # 房屋地址
    detail1 = "".join(detail).strip()  # 首尾去除空格和换行(默认)
    label1 = "".join(label)
    address1 = "".join(address).strip().replace(' ', '').replace('\n', '').replace('\xa0', '')  # 首尾去除空格和换行(默认)
    price = div.xpath('.//div[@class="zu-side"]//text()') # 价格
    price1 = "".join(price).replace(' ', '').replace('\n', '')
    print(title,detail1,address1,label1,price1)
