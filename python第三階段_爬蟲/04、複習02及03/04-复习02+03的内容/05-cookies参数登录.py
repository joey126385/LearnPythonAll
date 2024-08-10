'''
    cookies参数
    使用get方法中的cookies参数进行传递 注意：参数必须为字典类型或者cookiejar对象
# "home4399=yes; UM_distinctid=190e4da2ca5681-044f39f57072b1-26031c51-1fa400-190e4da2ca6a1d; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1721826422; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1721826422; HMACCOUNT=F635B7E3178EA351; _4399tongji_vid=172182642475659; _4399tongji_st=1721826424; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1721826425; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826425; _4399stats_vid=17218264249272447; USESSIONID=0462c1e9-a303-447d-b1c9-7115c43c648e; phlogact=l14027; Uauth=4399|1|2024724|my.|1721826443560|0e79329c6efeee20e47055025b6a31a0; Pauth=3503245786|2319398724|t3ce7n28137886eec06530703790dcc6|1721826443|10002|138a8f20baf12a692ee66603693cdbc2|2; ck_accname=2319398724; Puser=15348438633; Xauth=f4f4a1af57afa590a9bb4489e3f411d9; ptusertype=my.4399_login; Qnick=; Pnickset=1; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826442; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1721826442; Pmtime=3147614abec3fa318ec7%7C1721826444; ol=1"
    怎么用cookies参数传递
    页面复制过来的是字符串的cookie 要想办法 变成字典格式
    =前面的是key  后面的是value
    不同的键值对之间是 ; 隔开的
'''
import requests

# 请求传递登录后的cookie的写法  页面是在请求头里 我们也写在请求头里面
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

cookie_str = "home4399=yes; UM_distinctid=190e4da2ca5681-044f39f57072b1-26031c51-1fa400-190e4da2ca6a1d; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1721826422; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1721826422; HMACCOUNT=F635B7E3178EA351; _4399tongji_vid=172182642475659; _4399tongji_st=1721826424; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1721826425; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826425; _4399stats_vid=17218264249272447; USESSIONID=0462c1e9-a303-447d-b1c9-7115c43c648e; phlogact=l14027; Uauth=4399|1|2024724|my.|1721826443560|0e79329c6efeee20e47055025b6a31a0; Pauth=3503245786|2319398724|t3ce7n28137886eec06530703790dcc6|1721826443|10002|138a8f20baf12a692ee66603693cdbc2|2; ck_accname=2319398724; Puser=15348438633; Xauth=f4f4a1af57afa590a9bb4489e3f411d9; ptusertype=my.4399_login; Qnick=; Pnickset=1; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721826442; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1721826442; Pmtime=3147614abec3fa318ec7%7C1721826444; ol=1"
dict_cookie = {}
cookie_item = cookie_str.split("; ")  # 分割成每一个键值对  列表每一个值 就是cookie的键值对
for i in cookie_item:
    # print(i) # home4399=yes  key:value
    # dict_cookie['key'] = 'value' #赋值 语法格式
    # print(i.split('=')[0])
    # print(i.split('=')[1])
    dict_cookie[i.split('=')[0]] = i.split('=')[1]
print(dict_cookie)  # 变成键值对的cookie了 字典

url2 = "https://my.4399.com/forums/index-getMtags?type=game"  # 目标url
response = requests.get(url=url2, headers=headers2, cookies=dict_cookie)
response.encoding = "utf-8"
print(response.text)

'''
    复制cookie去爬取要登录网站 的两种方法
    两个方法作用都是一样的
    headers里
        只要页面复制一下就行
    cookies参数传递 
        要把复制的cookie进行转换 因为我们复制的是字符串 cookies参数要求传字典 或者cookiejar对象
    大部分情况 第一种
    第二种方法 
        我们用代码做模拟做模拟登录 拿到cookiejar对象或者字典
'''
