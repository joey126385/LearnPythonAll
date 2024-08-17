'''
    需求
        看到页面弹窗提示
    实现
        1： 定位到小方块
        2: 鼠标左键按住 不松开
        3： 往右边移动 实现往右拖拽
        4： 到达指定位置 松开鼠标左键

'''

from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链
import random


browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# iframe 页面嵌套了页面 获取内页面的内容直接是 定位不到
browser.switch_to.frame('iframeResult')  # 一般的内联框架都有ID  没有的话 可以写元素定位
# browser.switch_to.frame(browser.find_element_by_xpath()) # 没有的话 可以写元素定位
element =  browser.find_element_by_id('draggable')
action = ActionChains(browser)
#           2: 鼠标左键按住 不松开
action.click_and_hold(element)
# move_by_offset() 鼠标从当前位置移动到某个坐标
#         3： 往右边移动 实现往右拖拽
# action.move_by_offset(250, 0)
for i in range(5):
    action.move_by_offset(50, 0)
#         4： 到达指定位置 松开鼠标左键
action.release() # 松开鼠标左键
action.perform()  # 执行动作
