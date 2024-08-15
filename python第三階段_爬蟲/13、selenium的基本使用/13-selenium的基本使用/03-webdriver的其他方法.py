from selenium import webdriver
browser = webdriver.Chrome() # 首字母大写 谷歌选择谷歌
# 1：打开百度一下
browser.get('https://www.baidu.com/') # 方法里面传要访问的页面

print(browser.title) #  当前标签页标题
# browser.current_url # 当前url
print(browser.current_url)
# size 返回元素大小
print(browser.find_element_by_id('kw').size)
# text 获取元素的文本
print(browser.find_element_by_xpath('//span[@class="title-content-title"]').text)
print(browser.find_element_by_xpath('//div[@id="s-top-left"]/a').get_attribute('href'))
# is_display() 判断元素是否可见
print(browser.find_element_by_id('kw').is_displayed())
# is_enabled() 判断元素是否可用
print(browser.find_element_by_id('su').is_enabled())