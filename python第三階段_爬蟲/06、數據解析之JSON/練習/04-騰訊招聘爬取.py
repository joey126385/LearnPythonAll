import requests
import json

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
for i in range(1,11):
    url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722345350307&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex={i}&pageSize=10&language=zh-cn&area=tw"
    response = requests.get(url=url, headers=headers1)
    dict_text = json.loads(response.text) #　轉python 的dict
    Data1=dict_text["Data"]
    Data_Posts=Data1["Posts"]
    for d in Data_Posts :
        print(d.keys())
        print(d['RecruitPostName'])




