'''
    使用自动化爬取豆瓣top250的电影字段数据
    实现步骤：
        1：https://movie.douban.com/top250 操控打开对应的页面
        2： 对页面的内容做解析 lxml对数据进行解析
'''
from lxml import etree
from selenium import webdriver
browser = webdriver.Chrome() # 首字母大写 谷歌选择谷歌
# 1：打开百度一下
browser.get('https://movie.douban.com/top250') # 方法里面传要访问的页面

# 获取页面 源码
response_text = browser.page_source # 获取页面源码
# print(response_text)
tree = etree.HTML(response_text)
li_list = tree.xpath('//ol[@class="grid_view"]/li')
print(len(li_list))

for li in li_list:
    title = ''.join(li.xpath('.//div[@class="hd"]/a/span/text()')).replace('\xa0','')
    info = li.xpath('.//div[@class="bd"]/p[1]/text()')
    rating_num = li.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0] # 评分
    star = li.xpath('.//div[@class="bd"]//div[@class="star"]/span[4]/text()')[0] # 评价人数
    quote = li.xpath('.//div[@class="bd"]//p[@class="quote"]/span/text()')[0] # 评语
    str1 = ''.join(info).replace(' ', '').replace('\n', '').replace('\xa0', '')
    info1 = str1.split('...')[0]
    info2 = str1.split('...')[1]
    year = info2.split('/')[0]  # 年份
    country = info2.split('/')[1]  # 国家
    label = info2.split('/')[2]  # 标签
    try:
        director = info1.split('主演:')[0].replace('导演:', '')  # 导演
        to_star = info1.split('主演:')[1]+'...'  # 主演
    except Exception as e:
        director = info1.split('主')[0].replace('导演:', '')  # 导演
        to_star = '...'  # 主演
    print(title,rating_num,star,quote,year,country,label,director,to_star)