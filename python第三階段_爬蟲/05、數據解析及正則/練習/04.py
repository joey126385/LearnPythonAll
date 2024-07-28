import re
import requests

url1="https://www.douyu.com/g_TVgame"# 主机游戏
# 模擬真人
headers1={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
response = requests.get(url=url1, headers=headers1)
# 找想要得到的數據 找規則
"""
            "ioa": 0,
            "isShowUp": 0,
            "nn": "王拉奇",
            "oaid": 0,
            "ol": 2269332,
            "ot": 0,
            "rgrpt": 1,
            "rid": 11144156,
            "rn": "【小奶团】恭喜歪伯50级牌牌啦！",
"""
# 取得所有姓名
nn_name_list=re.findall('"nn":"(.*?)"',response.text)
print(f"nn_name\t 長度 {len(nn_name_list)}")
for i in range(0, len(nn_name_list)):
    print(f" {i}  == {nn_name_list[i]}")