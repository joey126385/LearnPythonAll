from selenium import webdriver
import time
# python文件名不要叫模块名字

# selenium常见报错
# 报错1：ValueError:Timeout valve connect was object object at 0x00002354CDD7F80>，but it must be an int,float op None,
# 原因：selenium与urllib3不兼容
# 解决：卸载urllib3 安装老版本 比如1.26.2就可以解决  pip uninstall  urllib3 再  pip install urllib3==1.26.2
browser = webdriver.Chrome() # 首字母大写 谷歌选择谷歌
# browser.maximize_window() # 窗口最大化
# browser.minimize_window() # # 窗口最小化
# browser.set_window_size(700,500) # 设置宽700 高500的浏览器窗口
browser.get('https://www.google.com.tw/') # 方法里面传要访问的页面
# time.sleep(1)
# browser.get('https://www.douban.com/') # get方法都是在一个标签页打开的页面
# time.sleep(1)
# browser.back() # 后退  百度
# time.sleep(1)
# browser.forward() # 前进 豆瓣
# time.sleep(1)
# browser.refresh() # 页面刷新
# time.sleep(1)
# browser.save_screenshot('test.png') # 当前窗口截图

#browser.close() # 关闭当前标签页
# browser.quit() # 关闭浏览器
