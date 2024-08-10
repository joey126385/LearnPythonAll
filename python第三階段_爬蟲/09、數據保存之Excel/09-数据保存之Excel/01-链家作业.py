''''
    https://cs.lianjia.com/zufang/
    需求
        爬取100页的租房字段 保存到本地
    实现
        1：明确每一页的url 想办法生成100页的链接
            https://cs.lianjia.com/zufang/ 第一页
            https://cs.lianjia.com/zufang/pg2/ 第二页
            https://cs.lianjia.com/zufang/pg4/ 第四页
            每一页的页数 通过pg来确定的 页数是依次递增的 pg1就是第一页
        2: 发起请求 获取响应
        3：xpath解析出租房字段

        出现真人验证 怎么办？
            原因 就是速度过快
            处理方法 1： 代理
                2： 放慢速度 time.sleep(2)  # 强制停止2秒
                3： 人工过一下验证 带上cookie去请求
'''
import time
import requests
from lxml import etree

headers1 = {
    "Cookie":"select_city=430100; lianjia_ssid=15167b2f-c94a-48b9-a3d8-43f6b91dce72; lianjia_uuid=5d45d295-de7e-46fa-a5f5-493c28fd2f0d; GUARANTEE_POPUP_SHOW=true; GUARANTEE_BANNER_SHOW=true; hip=abNcGQ9Nzru5sljKGe-SY-wnQ1ihshbngBH9zqj0vaPfANHjnh2mmDrKlF30RrMZPyjA0a3PZVXlOnjJ3FfZ_wGpOWn-70kvrEiCl_q24Ovu44s_ie7VBQ%3D%3D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYjdiNWQ1NTVjODljY2EyYzJlNTc0Y2YyMjVhNWU4NGQ3NmFlNmQwZjliYzNiODlmMDhlNmU1YjU2YmJlNWM4YTdiNGEyNmU5ODIzNjM3ZDQ5NGU4MjRjMjk4YzIxMGFkYzUwYWQxMzYwNzU5MzAzZGRlZGFiMzVmMTk1MDBjOTg5ODY1NDNiYmZhNjgwZWM5NjdlYmUzMzJmMDFhMmJjMmI5Mjc0YThjNjA4NjMxYWI4ZmQ5MDVkMzJhYWVmOGM4NTk3NjcxNGM2MGYyMmIyZjJlYzI0ZjdlM2Q5OTM2MzAxYjkzYjI0ZWEwM2JhZTg0NjEwMzQxNjQ1MjliYjUzOVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkOTY5ODIwOFwifSIsInIiOiJodHRwczovL2NzLmxpYW5qaWEuY29tL3p1ZmFuZy9wZzEwMC8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

for page in range(1, 101):
    url1 = f"https://cs.lianjia.com/zufang/pg{page}/"
    response = requests.get(url=url1, headers=headers1)

    # print(response.text) # 查看请求成功没 请求成功了
    tree = etree.HTML(response.text)
    print(f'=========第{page}页开始爬取===========')
    div_list = tree.xpath('//div[@class="content__list--item"]')
    print(len(div_list))
    for div in div_list:
        title = div.xpath('.//div[@class="content__list--item--main"]/p[1]/a/text()')[0].strip()  # 标题
        detail = div.xpath('.//div[@class="content__list--item--main"]/p[2]//text()')  # 房屋详情
        label = div.xpath('.//div[@class="content__list--item--main"]/p[3]//text()')  # 房屋标签
        source = div.xpath('.//div[@class="content__list--item--main"]/p[4]//text()')  # 房屋来源
        price = div.xpath('.//div[@class="content__list--item--main"]/span[@class="content__list--item-price"]//text()')  # 房屋详情
        detail1 = ''.join(detail).replace(' ', '').replace('\n', '')
        label1 = ''.join(label).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        source1 = ''.join(source).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        price1 = ''.join(price)
        print(title,detail1,label1, source1, price1)
    time.sleep(2)  # 强制停止2秒
    print(f'=========第{page}页爬取完毕===========')