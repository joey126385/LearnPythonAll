import requests

url1 = "https://www.google.com/"  # 国内访问不了

# response = requests.get(url=url1, timeout=3)  # 请求超过3秒就报错
# timeout=(3,7) (请求时间，响应时间) 请求超过
# 三秒报错 响应时间超过7秒报错
response = requests.get(url=url1, timeout=(3,7))  # 请求超过3秒就报错
print(response.text)
