'''
    需求
        模拟登录超级鹰网站 处理字符验证码
    实现
        1：https://www.chaojiying.com/user/login/
        2：定位到账号密码输入框 输入账号密码
        3：拿到验证码的图片 发给打码平台
        4：得到结果 在输入框进行输入
        5： 点击登录按钮
'''
from selenium import webdriver
from Chaojiying_Python.chaojiying import  Chaojiying_Client
browser = webdriver.Chrome()  # 首字母大写 谷歌选择谷歌

# 没问题的同学 可以下课了

def main():
    # 1：https://www.chaojiying.com/user/login/
    browser.get('https://www.chaojiying.com/user/login/')
    #  2：定位到账号密码输入框 输入账号密码
    browser.find_element_by_name('user').send_keys('nanfeng123')  # 输入账号
    browser.find_element_by_name('pass').send_keys('nanfeng')  # 输入密码
    # 3：拿到验证码的图片 发给打码平台
    element = browser.find_element_by_xpath('//form[@name="fm2"]/div/img')
    element.screenshot('chaojiying.png') # 对这个元素截图

    chaojiying = Chaojiying_Client('nanfeng123', 'nanfeng', '961271')	#用户中心>>软件ID 生成一个替换 96001
    im = open('chaojiying.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 1902)		 #发给打码平台
    #  4：得到结果 在输入框进行输入
    browser.find_element_by_name('imgtxt').send_keys(result['pic_str'])
    #  5： 点击登录按钮
    browser.find_element_by_class_name('login_form_input_submit').click()
main()
