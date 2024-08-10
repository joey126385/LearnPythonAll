import json

# 方式一
f = open('demo.json','r',encoding="utf-8")
json_str =  f.read()
f.close()

# show data
print(json_str,type(json_str))

# 將json字串 轉python的 dict字典   使用loads(jsonStr)
result =  json.loads(json_str)
print(result,type(result)) # <class 'dict'>

f = open('demo.json','r',encoding="utf-8")
result1 = json.load(f) # 传文件对象
print(result1,type(result1))


