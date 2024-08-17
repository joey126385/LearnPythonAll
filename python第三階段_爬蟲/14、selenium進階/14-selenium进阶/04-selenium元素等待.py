import time

from selenium import webdriver
'''
隐式等待
    即运行过程中，如果元素可以定位到，它不会影
    响代码运行，但如果定位不到，则它会以轮询的
    方式不断地访问元素直到元素被找到，若超过指
    定时间，则抛出异常。
'''
browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌
browser.implicitly_wait(20) # 隐式等待 等待20秒 #
browser.get('https://www.baidu.com/')  # 方法里面传要访问的页面 默认指向get页面
print(456)
# time.sleep(2) #强制等待 不太智能
browser.find_element_by_id('kw') # 元素定位 可以定位到
print(123)
browser.find_element_by_id('kw1') # 元素定位 可以定位到
print('abc')