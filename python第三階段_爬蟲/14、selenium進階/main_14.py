from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链
option = webdriver.ChromeOptions()
browser = webdriver.Chrome() # 首字母大写 谷歌选择谷歌
browser.get('https://movie.douban.com/top250') # 方法里面传要访问的页面
for page in range(0,11):
    tree = etree.HTML(browser.page_source)
    li_list = tree.xpath('//ol[@class="grid_view"]/li')
    for li in li_list:
        title = ''.join(li.xpath('.//div[@class="hd"]/a/span/text()')).replace('\xa0', '')
        info = li.xpath('.//div[@class="bd"]/p[1]/text()')
        rating_num = li.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]  # 评分
        star = li.xpath('.//div[@class="bd"]//div[@class="star"]/span[4]/text()')[0]  # 评价人数
        quote = li.xpath('.//div[@class="bd"]//p[@class="quote"]/span/text()')[0]  # 评语
        str1 = ''.join(info).replace(' ', '').replace('\n', '').replace('\xa0', '')
        info1 = str1.split('...')[0]
        info2 = str1.split('...')[1]
        year = info2.split('/')[0]  # 年份
        country = info2.split('/')[1]  # 国家
        label = info2.split('/')[2]  # 标签
        try:
            director = info1.split('主演:')[0].replace('导演:', '')  # 导演
            to_star = info1.split('主演:')[1] + '...'  # 主演
        except Exception as e:
            director = info1.split('主')[0].replace('导演:', '')  # 导演
            to_star = '...'  # 主演
        print(title, rating_num, star, quote, year, country, label, director, to_star)
    element=browser.find_element_by_xpath('//span[@class="next"]/a') # 后页>
    action = ActionChains(browser) # 動作鏈
    element.click() # 點擊動作
    action.perform()# 執行動作
    print("!!!!!!!")