'''
    使用自动化爬取豆瓣top250所有页的电影字段数据
    思路
        1： https://movie.douban.com/top250 打开页面
        2： 拖动滚动条到页面底部
        3： 获取页面数据 做数据解析
        4： 点击后页元素
        5： 走第二步
        6： 走第三步
        7： 走第四步
'''
import re
import time

from lxml import etree
from selenium import webdriver

browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌

def parse():
    # 获取页面 源码
    response_text = browser.page_source  # 获取页面源码
    # print(response_text)
    tree = etree.HTML(response_text)
    li_list = tree.xpath('//ol[@class="grid_view"]/li')
    print(len(li_list))

    for li in li_list:
        title = ''.join(li.xpath('.//div[@class="hd"]/a/span/text()')).replace('\xa0', '')
        info = li.xpath('.//div[@class="bd"]/p[1]/text()')
        rating_num = li.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]  # 评分
        star = li.xpath('.//div[@class="bd"]//div[@class="star"]/span[4]/text()')[0]  # 评价人数
        quote = li.xpath('.//div[@class="bd"]//p[@class="quote"]/span/text()')  # 评语
        if quote ==[]:
            quote=['暂未填写评语']
        else:
            quote= quote[0]
        str1 = ''.join(info).strip().replace(' ', '').replace('\xa0', '')
        info1 = str1.split('\n')[0]  # 导演+主演
        info2 = str1.split('\n')[1]  # 年份+国家+标签

        year = info2.split('/')[0]  # 年份
        country = info2.split('/')[1]  # 国家
        label = info2.split('/')[2]  # 标签

        director = re.findall('导演:(.*?)主', info1)  # 导演
        if director==[]:
            director = re.findall('导演:(.*?)\.\.\.', info1)[0]
        else:
            director=director[0]
        to_star = re.findall('主演:(.*?)\.\.\.', info1)  # 点在正则有特殊含义  斜杠转义一下
        if to_star == []:  # 有问题的数据 匹配就为空列表
            to_star = "...网站暂未填写"
        else:
            to_star = to_star[0]

        print(title, rating_num, star, quote, year, country, label, director, to_star)

def main():
    # 入口函数
    browser.get('https://movie.douban.com/top250')  # 方法里面传要访问的页面
    # 2： 拖动滚动条到页面底部
    browser.execute_script('window.scroll(0,document.documentElement.scrollHeight)')
    time.sleep(2)
    # 3： 获取页面数据 做数据解析
    parse()
    # 4： 点击后页元素
    # browser.find_element_by_xpath('//span[@class="next"]/a').click()
    for i in range(9):
        browser.find_element_by_xpath('//span[@class="next"]/a').click()
        time.sleep(1)
        browser.execute_script('window.scroll(0,document.documentElement.scrollHeight)')
        parse() # 解析数据


main()
