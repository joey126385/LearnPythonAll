"""
https://www.kuaidaili.com/free/ 目标页面
用正则匹配这一页所有的 IP PORT 匿名度
只要这三个 其他的不用做

"""
import re

import  requests
url1="https://www.kuaidaili.com/free/"
# 模擬真人
headers1={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
resp=requests.get(url=url1,headers=headers1)
#print(resp.text)
ip=re.findall('"ip": "(.*?)"',resp.text)
port=re.findall('"port": "(.*?)"',resp.text)
#ip=re.findall('"ip": "(.*?)",',resp.text)
print(f"ip  長度{len(ip)}")
print(f"port  長度{len(port)}")
for i in range(0,len(ip)):
    print(f"{i+1}\t{ip[i]}\t{port[i]} \t 高匿名")
#with open(f"a.html", "w", encoding="utf-8") as f:
   # f.write(resp.text)