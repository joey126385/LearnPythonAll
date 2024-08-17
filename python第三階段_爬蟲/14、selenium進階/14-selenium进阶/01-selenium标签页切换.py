import time

from selenium import webdriver

browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌
browser.get('https://www.baidu.com/')  # 方法里面传要访问的页面 默认指向get页面
time.sleep(2)
# 可以帮我们执行JS代码
browser.execute_script('window.open("https://www.douban.com")')  # 豆瓣
time.sleep(2)
browser.execute_script('window.open("https://cn.bing.com/")')  # 必应
time.sleep(2)
browser.execute_script('window.open("https://www.bilibili.com/")')  # B站
time.sleep(5)
# 1. 获取所有标签页的窗口句柄
window = browser.window_handles  # 返回列表
# 2. 利用窗口句柄 切换到句柄指向的标签页 switch_to.window()
for win in window:
    browser.switch_to.window(win)  # 切换标签页
    print(browser.title)
    time.sleep(2)
#  注意 多个窗口切换的情况 JS打开的窗口是倒序插入
# 我们代码切换顺序  百度  哔哩哔哩  必应    豆瓣
# 我们页面看的排序  百度  豆瓣     必应   哔哩哔哩
