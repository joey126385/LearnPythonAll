'''
    直接拿cookie登录
'''
import requests

headers1 = {
    # cookie直接是登录后的cookie 告诉代码我现在是登录后的信息
    "Cookie": "_4399tongji_vid=172165438727089; _4399tongji_st=1721654387; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721654387; HMACCOUNT=43CA87EC95396F77; _4399stats_vid=17216543873137803; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1721654387; USESSIONID=d2b8c1dd-1b57-446d-928f-76f00316e91f; Puser=15348438633; ptusertype=my.4399_login; Qnick=; Pnickset=1; _gprp_c=""; Pnick=0; phlogact=l15037; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1721654638; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1721654638; Uauth=4399|1|2024722|my.|1721655282425|e98b0c7d1810ce1f003a9a3152d45ee1; Pauth=3503245786|2319398724|t3ce7n28132d12a106447898ba482461|1721655282|10002|6b8a32e3890b40e1ca2b50f4f658a004|2; ck_accname=2319398724; Xauth=0f38f2b20e90c0c849c57986a8a1bc55",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url="https://my.4399.com/forums/index-getMtags?type=game", headers=headers1)
response.encoding = "utf-8"
print(response.text)  # 直接登录成功了
