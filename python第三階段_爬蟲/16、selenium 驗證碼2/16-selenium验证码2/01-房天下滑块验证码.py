'''
    需求
        处理房天下滑块验证码
    思路
    1： 访问 https://passport.fang.com/?backurl=https%3A%2F%2Fwww1.fang.com%2F
    2： 点击账号密码登录
    3： 定位账号密码输入框 输入账号密码
    4： 点击登录 出现滑块验证码
    5： 获取验证码的图片
    6： 发给打码平台 返回缺口坐标给我们
    7： 生成滑块轨迹 进行拖动
'''
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链

from Chaojiying_Python.chaojiying import Chaojiying_Client

browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌
browser.maximize_window()
# 伪装身份
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () =>false }) """})


def main():
    #  1： 访问 https://passport.fang.com/?backurl=https%3A%2F%2Fwww1.fang.com%2F
    browser.get("https://passport.fang.com/?backurl=https%3A%2F%2Fwww1.fang.com%2F")
    time.sleep(1)
    # 2： 点击账号密码登录
    browser.find_element_by_xpath('//div[@class="login-cont"]/dt/span[2]').click()
    #   3： 定位账号密码输入框 输入账号密码
    browser.find_element_by_id('username').send_keys('134567899012')  # 输入账号
    time.sleep(1)
    browser.find_element_by_id('password').send_keys('134567899012asd')  # 输入密码
    time.sleep(1)
    # 4： 点击登录 出现滑块验证码
    browser.find_element_by_id('loginWithPswd').click()
    #   5： 获取验证码的图片
    time.sleep(2)
    element = browser.find_element_by_class_name('img-bg')  # 定位验证码图片元素
    src_url = element.get_attribute('src')  # 图片的链接
    # element.screenshot('ftx.png') # 不能截图 元素在页面不可见
    # print(src_url)
    with open('ftx.png', 'wb')as f:
        f.write(requests.get(url=src_url).content)
    # 6： 发给打码平台 返回缺口坐标给我们
    chaojiying = Chaojiying_Client('nanfeng123', 'nanfeng', '961271')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('ftx.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 9101)  # 验证码类型
    x = result['pic_str'].split(',')[0]  # 取出X坐标
    print(x)
    # 7： 生成滑块轨迹 进行拖动
    tracks = get_track(int(x))  # 转换类型 传递 调用函数 会有返回值 返回值是轨迹列表 用变量接收
    print(tracks)
    drop = browser.find_element_by_xpath('//div[@class="drag-handler verifyicon center-icon"]')
    action = ActionChains(browser) # 动作链实例化 传浏览器驱动对象
    action.click_and_hold(drop)  # 按住不松开
    for i in tracks:
        # move_by_offset() 鼠标从当前位置移动到某个坐标
        action.move_by_offset(i,0)
    action.release() # 松开鼠标左键
    action.perform() # 执行动作链

def get_track(x):
    # 初速度
    v = 0
    # 单位时间，统计轨迹 多时间内的位置
    t = 0.3
    # t = random.randint(2, 3) / 10
    # 轨迹列表
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值的时候减速 前4/5段加速 后1/5减速
    mid = x * 4 / 5
    while current < x:
        if current < mid:
            a = random.randint(12, 13)  # 加速
            # a = 2
        else:
            # a = -3  # 减速
            a = -random.randint(12, 13)  # 减速
        v0 = v
        v = v0 + a * t
        # 位移公式: s=V0t+(at^2)/2
        s = v0 * t + 1 / 2 * a * t * t
        # 当前位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))
    # 反着滑动大概位置
    for i in range(3):
        tracks.append(-random.randint(12, 13))
    return tracks


main()
