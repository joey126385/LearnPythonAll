import json


# 读取文件的json字符串的数据
# f = open('demo.json','r',encoding="utf-8")
# json_str =  f.read()
# f.close()

# print(type(json_str)) # <class 'str'>
#  json.loads() 将JSON字符串转为python类型
# result =  json.loads(json_str) # 将要转换的数据传进去就行
# print(result,type(result)) # <class 'dict'>
# print(result['a'])
# json.load() 读取文件中json形式的字符串 转为python


f = open('demo.json','r',encoding="utf-8")
result = json.load(f) # 传文件对象
print(result,type(result))
