list1 = ['\n                            导演: 加布里尔·穆奇诺 Gabriele Muccino\xa0\xa0\xa0主演: 威尔·史密斯 Will Smith ...',
         '\n                            2006\xa0/\xa0美国\xa0/\xa0剧情 传记 家庭\n                        ']

str1 = ''.join(list1).replace(' ', '').replace('\n', '').replace('\xa0', '')
info1 = str1.split('...')[0]
info2 = str1.split('...')[1]
year = info2.split('/')[0] # 年份
country = info2.split('/')[1] # 国家
label = info2.split('/')[2] # 标签
print(info1)
director = info1.split('主演:')[0].replace('导演:', '')  # 导演
to_star = info1.split('主演:')[1]  # 主演
print(director)
