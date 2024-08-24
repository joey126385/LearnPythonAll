'''
    需求
        处理B站点选验证码
    实现
        1： 访问 https://www.bilibili.com/
        2： 点击登录 出现登录页面
        3： 输入账号密码 点击登录
        4:  对 class geetest_holder geetest_silver 的元素截图  拿到验证码图片
        5：发给打码平台 获取坐标位置
        6： 动作链操作 根据坐标 移动到坐标位置 依次点击
        7： 点确认
'''
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from Chaojiying_Python.chaojiying import Chaojiying_Client

browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌
browser.maximize_window()
# 伪装身份
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () =>false }) """})

browser.implicitly_wait(10)


def main():
    # 1： 访问 https://www.bilibili.com/
    browser.get("https://www.bilibili.com/")
    # 2： 点击登录 出现登录页面
    browser.find_element_by_xpath('//div[@class="header-login-entry"]').click()
    # 3： 输入账号密码 点击登录
    browser.find_element_by_xpath('//div[@class="form__item"][1]/input').send_keys("1231231")
    browser.find_element_by_xpath('//div[@class="form__item"][2]/input').send_keys("asdasdas1231")
    browser.find_element_by_xpath('//div[@class="btn_primary "]').click()
    time.sleep(2)
    # 4:  对 class geetest_holder geetest_silver 的元素截图  拿到验证码图片
    element = browser.find_element_by_xpath('//div[@class="geetest_holder geetest_silver"]')
    element.screenshot("bili.png")  # 截图验证码
    # 5：发给打码平台 获取坐标位置
    chaojiying = Chaojiying_Client('nanfeng123', 'nanfeng', '961271')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('bili.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 9004)['pic_str']  # 验证码类型
    # '148,118|237,112|110,256|191,276'
    # print(result)
    pic_str_list = result.split('|')  # 以|得到每一个字 返回列表
    #  6： 动作链操作 根据坐标 移动到坐标位置 依次点击
    action = ActionChains(browser) # 动作链实例化
    for i in pic_str_list:  # 循环得到每一个字
        print(i)  # 148,118
        x = int(i.split(',')[0])  # X轴
        y = int(i.split(',')[1])  # Y轴
        # move_to_element_with_offset() #  移动到距某个元素（左上角坐标）多少距离的位置
        action.move_to_element_with_offset(element,x,y).click()
    action.perform()
    # 7： 点确认
    browser.find_element_by_xpath('//div[@class="geetest_commit_tip"]').click()
main()
