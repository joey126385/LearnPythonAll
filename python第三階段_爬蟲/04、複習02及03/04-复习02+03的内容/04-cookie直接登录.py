'''
    直接使用页面 目标url的cookie值去访问
    这个cookie值是登录后的
    cookie的值是请求头的headers里
'''
# headers1 = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }
# response = requests.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1)
# response.encoding = "utf-8"
# print(response.text)  # 爬取失败 # 代码他现在知道我们登陆了吗？不知道 访问页面 默认是没有的登录的
# 我们需要告诉他 我们现在的状态是 登录了的状态
import requests
# 请求传递登录后的cookie的写法  页面是在请求头里 我们也写在请求头里面
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie": "home4399=yes; UM_distinctid=190e4da2ca5681-044f39f57072b1-26031c51-1fa400-190e4da2ca6a1d; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1721826422; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1721826422; HMACCOUNT=F635B7E3178EA351; _4399tongji_vid=172182642475659; _4399tongji_st=1721826424; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1721826425; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826425; _4399stats_vid=17218264249272447; USESSIONID=0462c1e9-a303-447d-b1c9-7115c43c648e; phlogact=l14027; Uauth=4399|1|2024724|my.|1721826443560|0e79329c6efeee20e47055025b6a31a0; Pauth=3503245786|2319398724|t3ce7n28137886eec06530703790dcc6|1721826443|10002|138a8f20baf12a692ee66603693cdbc2|2; ck_accname=2319398724; Puser=15348438633; Xauth=f4f4a1af57afa590a9bb4489e3f411d9; ptusertype=my.4399_login; Qnick=; Pnickset=1; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826442; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1721826442; Pmtime=3147614abec3fa318ec7%7C1721826444; ol=1"
}
url2 = "https://my.4399.com/forums/index-getMtags?type=game" # 目标url
response = requests.get(url=url2,headers=headers2)
response.encoding="utf-8"
print(response.text) # 已经成功爬取了 一个已经登录了的情况
'''
    爬虫本质是什么？
    模拟真人
    真人访问这个链接 可以成功访问 因为登录状态是登录后 登录后可以访问这页面
    识别这个cookie 真人通过cookie告诉人家网站 我已经登录了 
    爬虫是模拟真人 真人带这个cookie能访问 爬虫去带这个cookie 也可以模拟成真人 访问登录后的页面
'''