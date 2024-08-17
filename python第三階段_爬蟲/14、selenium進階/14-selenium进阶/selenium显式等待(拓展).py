"""
    第三种办法就是显式等待，WebDriverWait，配合该类的until()和until_not()方法，就能够根据判断条件而进行灵活地等待了。
    它主要的意思就是：程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
    poll_frequency:检测间隔时间，默认0.5s

    隐式等待 全局变量 作用于全局
    显式等待 局部变量 作用于指定元素
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # 提供预期判断的方法，指定等待的元素,能够完成什么操作
from selenium.webdriver.support.wait import WebDriverWait # 显式等待
from selenium.webdriver.common.by import By  #  定位元素

base_url = "http://www.baidu.com"
browser = webdriver.Chrome()

# locator = (By.ID, 'kw')
browser.get(base_url)

print(WebDriverWait(browser, 10).until(EC.title_is("百一下，你就知道")))
'''判断title,返回布尔值'''

print(WebDriverWait(browser, 10).until(EC.title_contains("百度一下")))
'''判断title，返回布尔值'''

print(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'kw'))))
'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''

print(WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'su'))))
'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

print(WebDriverWait(browser, 10).until(EC.visibility_of(browser.find_element(by=By.ID, value='kw'))))
'''判断元素是否可见，如果可见就返回这个元素'''


print(WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mnav'))))
'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''

print(WebDriverWait(browser, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.mnav'))))
'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''

print(WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="s-usersetting-top"]'), u'设置')))
'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''

print(WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#su'), u'百度一下')))
'''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''

# WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
# 注意这里并没有一个frame可以切换进去



print(WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s-usersetting-top"]'))))
'''判断某个元素中是否可见并且是enable的，代表可点击'''

browser.close()
'''
****************expected_conditions类提供的预期条件判断的方法****************
title_is   判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值
title_contains 判断当前页面的 title 是否包含预期字符串，返回布尔值
presence_of_element_located    判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见
visibility_of_element_located  判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于 0
visibility_of  跟上面的方法做一样的事情，只是上面的方法要传入 locator，这个方法直接传定位到的 element 就好了
presence_of_all_elements_located   判断是否至少有 1 个元素存在于 dom 树中。举个例子，如果页面上有 n 个元素的 class 都是'column-md-3'，那么只要有 1 个元素存在，这个方法就返回 True
text_to_be_present_in_element  判断某个元素中的 text 是否 包含 了预期的字符串
text_to_be_present_in_element_value    判断某个元素中的 value 属性是否包含 了预期的字符串
frame_to_be_available_and_switch_to_it 判断该 frame 是否可以 switch进去，如果可以的话，返回 True 并且 switch 进去，否则返回 False
invisibility_of_element_located    判断某个元素中是否不存在于dom树或不可见
element_to_be_clickable    判断某个元素中是否可见并且是 enable 的，这样的话才叫 clickable
staleness_of   等某个元素从 dom 树中移除，注意，这个方法也是返回 True或 False
element_to_be_selected 判断某个元素是否被选中了,一般用在下拉列表
element_selection_state_to_be  判断某个元素的选中状态是否符合预期
element_located_selection_state_to_be  跟上面的方法作用一样，只是上面的方法传入定位到的 element，而这个方法传入 locator
alert_is_present   判断页面上是否存在 alert
*****************************************************************************
'''