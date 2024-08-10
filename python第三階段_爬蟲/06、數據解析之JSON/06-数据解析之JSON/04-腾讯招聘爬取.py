'''
        https://careers.tencent.com/search.html?query=at_1
        腾讯招聘的网站
        需求： 爬取这个页面的招聘字段信息
        实现思路
            1：明确目标url
                确定一下岗位的数据 在那个页面里面
                https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722257867740&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
                GET 请求
            2： 发起请求 获取响应
                页面的数据 拿到本地
            3： JSON数据的解析
                从内容里面提取出 招聘的字段
            页面一条数据 有多个字段的信息(城市 时间 标题这样的字段)
            页面有多条数据 我们是要爬多条
            我们希望是
                数据一一对应   爬第一条数据  拿到第一条数据的所有字段 爬第二条 拿到第二条数据的所有字段
               还是 数据所有的字段放一块  所有的数据的标题 放一起  城市放一起 时间放一起
            我们肯定是要一条数据放一块的
        实现一一对应
            获取到每一条数据 取出每一条数据的字段
        页面每一条数据 都是字典格式
        所有的数据在一个列表里面  [{},{},{}]
'''
import requests
import json
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
url1 = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722257867740&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
response = requests.get(url=url1, headers=headers1)
# print(response.text) # 成功拿到数据
#  对于json字符串 一定要把层级关系搞清楚 我们要的数据在哪个层级下面
res_text = json.loads(response.text) # JSON字符串 转为python的数据类型
print(type(res_text))
# print(res_text["Data"]['Posts']) # [{},{},{}]
for data in res_text["Data"]['Posts']: # 循环取出每一条数据
    # data {}
    LastUpdateTime = data['LastUpdateTime'] # 时间
    LocationName = data['LocationName'] # 城市
    RecruitPostName = data['RecruitPostName'] # 岗位标题
    Responsibility = data['Responsibility'] # 岗位职责
    Responsibility = Responsibility.replace('\r\n','') # 字符串替换 把\r\n替换成空
    print(LastUpdateTime,LocationName,RecruitPostName,Responsibility)
    print("===========================")

