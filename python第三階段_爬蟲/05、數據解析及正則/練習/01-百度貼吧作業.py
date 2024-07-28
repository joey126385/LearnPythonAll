"""
    題目：
        爬取五个贴吧的内容(只要爬1页)保存到本地html
        https://tieba.baidu.com/index.html?
"""
import  requests
# url1="https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D"
# 模擬真人
headers1={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
kw = ["抗压吧", "DNF", "逆水寒", "魔兽世界", "永劫无间"]
for i in kw :
    url1 = f"https://tieba.baidu.com/f?kw={i}"
    response=requests.get(url=url1,headers=headers1)
    with open(f"{i}.html","w",encoding="utf-8") as  f:
        f.write(response.text)