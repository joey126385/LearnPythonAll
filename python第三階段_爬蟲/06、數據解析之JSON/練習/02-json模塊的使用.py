import json

# 一般dict  key value
dict1 = {"a": 1, "b": 2}
# 將字典轉為json字串
# 方式一 使用dumps(dict) 將python數據轉乘json字串
result01=json.dumps(dict1)
print(result01,type(result01))

#方式二 使用強制轉型
result02=str(dict1)
print(result02,type(result02))

# 方式三 使用賦值
dict1[(2, 1)] = "元祖"
# 因 字典轉json 格式錯誤  需要加上 skipkeys=True 過濾不是json數據
# print("錯誤",json.dumps(dict1))
print(json.dumps(dict1, skipkeys=True))

# 寫入中文 中文會變成 unicode碼 需要加上 ensure_ascii=False)
# 賦值 中文
dict1["c"] = "你好嗎"
with open("demo.json","w",encoding="utf-8")as f:
    # 方式一
    # json.dump(dict1,f,skipkeys=True, ensure_ascii=False)有編碼問題
    # 方式二
    f.write(json.dumps(dict1, skipkeys=True, ensure_ascii=False))