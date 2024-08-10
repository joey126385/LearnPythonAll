'''
    模块下载  默认是最新 5.2
    pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple
    # -i https://pypi.tuna.tsinghua.edu.cn/simple 换成国内镜像 下载 比  pip install lxml安装的速度更快
    如果导包没有 etree 回退一下版本 就可以解决
        pip uninstall lxml 卸载命令
        pip install lxml==4.9.2  ==是指定版本安装 后面跟上版本号

'''

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

tree =  etree.HTML(str1) # 把我们要解析的数据 传进去 变成 Element对象
# print(tree)
# print(type(tree)) #  Element
# print(etree.tostring(tree))
#  xpath方法里写规则匹配我们要的数据 // 从当前节点选取子孙节点
# 重点掌握 / //  @ []  这个四个 最主要用
print(tree.xpath('//li')) # 所有li
print(tree.xpath('//ul/li')) # 所有li
print(tree.xpath('//ul//li')) # 所有li
print(tree.xpath('//div//li')) # 所有li
# 匹配数据数据的写法规则很多 只要能拿到数据就行
print(tree.xpath('//div//li/@class')) # @ 获取li的class属性
#写条件过滤
print(tree.xpath('//div//li[@class="item-0"]')) # [ ] 写条件过滤
print(tree.xpath('//div//li[1]/a/text()')) #text() 获取标签的内容   [1] 拿第一个li xpath索引从1开始

print(tree.xpath('//div//li[1]//text()')) # 第一个Li下所有的内容
print(tree.xpath('//div//li[last()]//text()')) # 最后Li下所有的内容

# 点表示当前节点 点点 当前的父级
print(tree.xpath('//li/..'))
# * 通配符 匹配任何元素节点
print(tree.xpath('//*[@aaa="南风"]'))
print(tree.xpath('//li[@*]'))

# |  选取若干节点(多个规则去匹配元素) 每个规则互不干扰
print(tree.xpath('//li[@aaa="南风"] | //a[@href="link1.html"]/text() '))


