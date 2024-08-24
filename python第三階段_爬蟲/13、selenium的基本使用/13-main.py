#   導包
from selenium import webdriver
import time

# 選擇瀏覽器
browser = webdriver.Chrome()
# 開啟網站
browser.get('https://www.google.com.tw/')
def L13_01():
    # 選擇瀏覽器
    browser = webdriver.Chrome()
    # 開啟網站
    browser.get('https://www.google.com.tw/')

    # 視窗最大化
    browser.maximize_window()

    # # 視窗最小化
    # browser.minimize_window()

    # 自定義大小 例 瀏覽器 寬 600 高 700
    browser.set_window_size(600, 700)

    # 當前窗口截圖
    browser.save_screenshot('test.png')

    # 刷新頁面
    browser.refresh()

    # 上一頁
    browser.back()

    # 下一頁
    browser.forward()

    # 關閉當前頁籤
    browser.close()

    # 關閉瀏覽器
    browser.quit()

    # 當前標籤頁標題
    browser.title

    # 當前URL
    browser.current_url

    # 返回元素大小

    # 獲取元素的文本

    # 要獲取的屬性

    # 判斷元素是否可見

    # 判斷元素是否可用

def L13_02():
    # 選擇瀏覽器
    browser = webdriver.Chrome()
    # 開啟網站
    browser.get('https://www.baidu.com/')

    #   ID 定位
    # send_keys 模擬鍵盤輸入的值
    browser.find_element_by_id('kw').send_keys('test')

    # class 定位
    browser.find_element_by_class_name('s_ipt').send_keys('selenium3')

    # name 定位
    browser.find_element_by_name('wd').send_keys('test')


    # css 選擇器定位
    browser.find_element_by_css_selector('#kw').send_keys('selenium4')

    # xpath 定位
    browser.find_element_by_xpath('//input[@id="kw"]').send_keys("selenium5")

    # 點籍
    browser.find_element_by_id('su').click()

def L13_03():
    browser.get('https://www.baidu.com/')  # 方法里面传要访问的页面 默认指向get页面
    time.sleep(2)
    # 可以帮我们执行JS代码
    browser.execute_script('window.open("https://www.douban.com")')  # 豆瓣
    time.sleep(2)
    browser.execute_script('window.open("https://cn.bing.com/")')  # 必应
    time.sleep(2)
    browser.execute_script('window.open("https://www.bilibili.com/")')  # B站
    time.sleep(5)

def L13_04():
    pass

L13_03()