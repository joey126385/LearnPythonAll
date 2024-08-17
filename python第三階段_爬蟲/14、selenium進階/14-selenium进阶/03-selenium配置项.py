from selenium import webdriver

option = webdriver.ChromeOptions()  # 实例化配置对象
ua = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.70 Safari/537.36'
# option.add_argument('--proxy-server=http://ip:port') # 更换ip
# option.add_argument(f'User-Agent={ua}') # 更换UA

# option.add_argument('--headless') # 指定无头模式 无界面启动
browser = webdriver.Chrome(options=option)
# 伪装身份
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () =>false }) """})
browser.get("http://httpbin.org/get")
# print(browser.page_source)
