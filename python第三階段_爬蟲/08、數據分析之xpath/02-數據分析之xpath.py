str1 = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html" text="shadjfhjisdf">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html" class="test">fourth item</a></li>
         <li aaa="南风" class="item-0"><a class="test" href="link5.html">fifth item</a></li>
     </ul>
</div>
"""

from lxml import etree

# 第一步 放入數據
tree =  etree.HTML(str1)

# 看內容
# print(tree) # <Element html at 0x1f8817c8500>
# print(type(tree)) # <class 'lxml.etree._Element'>
# print(etree.tostring(tree))

# 找所有li
"""
常用的
1、 //   从当前节点选取子孙节点
2、  /   从当前节点选取直接子节点
3、  @   獲取該屬性裡面的值
4、  []  過濾條件

//text()  列印內容
"""
m_1=tree.xpath('//li')
# print(len(m_1),m_1)
m_2=tree.xpath('//ul//li')
# print(len(m_2),m_2)
# print(tree.xpath('//div//li'))

m_3=tree.xpath('//ul/li')
# print(len(m_3),m_3)

# 獲取li 的 class 裡面的值
# print(tree.xpath('//div//li/@class'))

# 過濾條件
m=tree.xpath('//ul//li[@class="item-0"]')

# 列印內容
m=tree.xpath('//ul//li[@class="item-0"]//text()')
print(len(m),m)

