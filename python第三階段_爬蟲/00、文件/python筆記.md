

# python 爬蟲基礎

curlconverter.com

## 	1.request 模塊



## 	2.數據解析之正則

- https://www.douyu.com/g_TVgame
- https://www.kuaidaili.com/free/



導包：

```python
import re
```



**規則表達式==>符號**

| 符號代號 | 符號名稱                  |
| -------- | ------------------------- |
| .        | 匹配任意字串 除了換行符號 |
| *        | 匹配0個或者多個           |
| +        | 匹配一個或者多個          |
| ?        | 匹配0個或者一個           |
| \s       | 空白字串                  |
| \d       | 數字                      |



**正則表達式==>方法**

| 方法名稱     | 方法中文解析                                                 |
| ------------ | ------------------------------------------------------------ |
| re.match()   | 查找字串頭部 一次匹配要找到了 一個匹配的結果就返回<br />而不是查找所有匹配的結果。<br />print(re.match('www', 'www.runoob.com').span()) <br />print(re.match('com', 'www.runoob.com')) |
| re.findall() | 查找所有匹配的結果 然後返回列表。<br />中文的Unicode的编码范围主要在[\u4e00-\u9fa5]<br />result=re.findall("[\u4e00-\u9fa5]",str2) |
| re.split()   | 按照能夠匹配的子串將字串分割後返回列表。                     |
| re.sub()     | 方法用於替換。                                               |



總結:





## 	3.數據解析之json



## 	4.數據解析之BS4



## 	5.數據分析之xpath



lxml 模塊

- pip install lxml   		下載命令
- lxml  是一個html/xml 文件的解析器 主要的功能就是如何提取和解析HTML 或者 xml的數據



常用規則

| 代號   | 功能名稱                           |
| ------ | ---------------------------------- |
| /      | 從當前節點選取直接子節點           |
| //     | 從當前節點選取子孫節點             |
| .      | 選取當前節點                       |
| ..     | 選取當前節點的父節點               |
| @      | 選取屬性                           |
| last() | 選取最後一個                       |
| *      | 通配符 匹配任何屬性節點            |
| @*     | 匹配任何屬性節點                   |
| \|     | 選取若干節點 ( 多個規則去匹配元素) |



xpath使用

- from lxml import etree
- tree = etree.HTML(str1)
- tree.xpath(規則)



## 	6.數據保存之Excel



```shell
pip install  xlwt  -i https://pypi.tuna.tsinghua.edu.cn/simple 
pip install  xlrd  -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install  xlutils -i https://pypi.tuna.tsinghua.edu.cn/simple
```



## 	7.數據儲存之MySQL

```python
 pip install pymysql
import pymysql
```











