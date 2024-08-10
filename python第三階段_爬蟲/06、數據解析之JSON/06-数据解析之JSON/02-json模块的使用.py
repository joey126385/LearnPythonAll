'''
        json字符串 转python数据类型
        python数据类型 转JSON字符串
        有这样的模块 提供方法给我们使用
        json
'''
import json

dict1 = {"a": 1, "b": 2}
# 字典转为 JSON字符串
# 将python的数据类型转成json字符串
result = json.dumps(dict1)  # 把我们要转换的数据传进去就行了
print(result, type(result))  # <class 'str'> json字符串的类型
print(type(str(dict1)))  # <class 'str'> 不是JSON字符串
dict1[(2, 1)] = "元祖" # 字典赋值

print(dict1)
# keys must be str, int, float, bool or None, not tuple
# print(json.dumps(dict1)) # JSON 字符串的key不能是元祖 格式要求
# {"a": 1, "b": 2}
print(json.dumps(dict1, skipkeys=True))  # skipkeys=True 转换类型会出错的数据 过滤掉
dict1["c"] = "南风"
print(dict1)
# ensure_ascii= False 解决编码
# print(json.dumps(dict1, skipkeys=True, ensure_ascii=False))  # 中文会Unicode的编码
# open()

with open("demo.json","w",encoding="utf-8")as f:
    # f.write(str(dict1)) # 不是JSON字符串
    # 将python类型转为JSON并写入文件 # 参数1 我们要转写入到文件的数据, 参数2  文件对象
    # json.dump(dict1,f,skipkeys=True, ensure_ascii=False)
    #  write写入数据到文件  我写入一个JSON数据到JSON文件 会有问题吗？
    f.write(json.dumps(dict1, skipkeys=True, ensure_ascii=False))
