'''
    把这个腾讯招聘爬10页 取出数据就行 不用保存
    提示：
        每一页有对应的url
        第一页有个链接表示这个是第一页
        第二页有个链接表示这个是第二页
        每一页的链接会不一样
    多页爬取
        每一页的url链接是啥
        第二页
        https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722425953459&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn
        第三页
        https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722426000921&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex=3&pageSize=10&language=zh-cn&area=cn
        第四页
        https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722426031277&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex=4&pageSize=10&language=zh-cn&area=cn
        找url的不同的点 目的 为了我们能快速生成每一页的url 说白了 就是找规律
        pageIndex 每一页都不一样 他的值 就对应页数 数字依次递增
        timestamp 我们目前不知道是啥  可以测试一下这个值固定或者不传也能成功
        每一页的url 只有 pageIndex比较重要 会变化 代表页数
        可以根据这个规律 循环生成每一页的url
        翻页爬取小结
            有翻页我们点翻页 去找每一页的url
            找每一页url不同的地方 看看能不能通过代码生成每一页的url
            通过循环 按照规律 生成每一页的url
        步骤
            1： 10页的目标url
            2： 发起请求 获取响应
            3: 解析我们想要的数据
'''
import requests
import json
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
for i in range(1,11):
    # 循环 使用f插值法生成每一页的url
    url_index = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1722426031277&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=&pageIndex={i}&pageSize=10&language=zh-cn&area=cn"
    print(url_index)
    response= requests.get(url=url_index,headers=headers1)# 请求写在循环里面

    result_data = json.loads(response.text) # json转python
    # print(type(result_data))
    # print(result_data)
    # print(result_data['Data'])
    # print(result_data['Data']['Count'])
    for data in result_data['Data']['Posts']:
        LastUpdateTime = data['LastUpdateTime']  # 时间
        LocationName = data['LocationName']  # 城市
        RecruitPostName = data['RecruitPostName']  # 岗位标题
        Responsibility = data['Responsibility']  # 岗位职责
        Responsibility = Responsibility.replace('\r\n', '')  # 字符串替换 把\r\n替换成空
        print(LastUpdateTime, LocationName, RecruitPostName, Responsibility)
        print("===========================")
