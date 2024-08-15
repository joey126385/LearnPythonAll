'''
    需求
        在百度页面的输入框 输入指定的内容 点击百度一下搜索
    真人步骤
        1：打开百度一下
        2：输入框输入关键字   需要---》 定位到这个输入框
        3： 点击百度一下      需要---》 定位到百度一下的按钮
    find_element
        匹配第一个符合条件的  返回这个元素
    find_elements
        匹配所有符合条件的 返回的是列表
'''

from selenium import webdriver
browser = webdriver.Chrome() # 首字母大写 谷歌选择谷歌
# 1：打开百度一下
browser.get('https://www.baidu.com/') # 方法里面传要访问的页面
# 2. 定位到这个输入框
# send_keys 输入键盘键位 也可以输入指定的字符串
browser.find_element_by_id('kw').send_keys('selenium1') # 通过ID定位
browser.find_element_by_name('wd').send_keys('selenium2') # 通过name定位
browser.find_element_by_class_name('s_ipt').send_keys('selenium3') # 通过class定位
# css选择器 在里面写css选择器的代码
browser.find_element_by_css_selector('#kw').send_keys('selenium4')
# xpath定位 在里面写xpath的代码
browser.find_element_by_xpath('//input[@id="kw"]').send_keys("selenium5")
# 3. 定位到百度一下的按钮
print(browser.find_element_by_id('su'))
browser.find_element_by_id('su').click() # 点击