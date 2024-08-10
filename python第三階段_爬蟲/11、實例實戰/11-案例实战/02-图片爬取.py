'''
    图片 视频 音频 只需要找到对应url 直接请求就可以了 数据都是二进制的
    文本数据 大多数都是字符串
    https://pic.netbian.com/4k/index.html 彼岸图网链接
    爬取这个网站10页的数据图片 保存到本地
    思路分析
        1：找到每一页的url
            https://pic.netbian.com/4k/index.html 第一页
            https://pic.netbian.com/4k/index_2.html 第二页
            https://pic.netbian.com/4k/index_3.html 第二页
            index_page page就是对应的页数 第一页是额外的 不符合规律 就是index
        2: 发起请求获取响应
        3： 解析数据 xpath解析
            图片名字 图片的链接  我们想要爬大图
            大图在详情页  列表的响应的没有大图 再次请求详情页  拿到详情页的响应 因为大图的下载链接在里面
            请求所有的详情页url 才能拿到每一条数据的大图下载链接
            列表页 包含了 所有的详情页url
            总结： 请求列表页---》列表页取出每一个详情页的url----》请求详情页---》取出大图的下载链接
        4： 保存到本地
'''
import requests
from lxml import etree

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def main():
    for page in range(1, 11):
        if page == 1:
            # 第一页用index
            url1 = "https://pic.netbian.com/4k/index.html"
        else:
            url1 = f"https://pic.netbian.com/4k/index_{page}.html"
        response = requests.get(url=url1, headers=headers1)
        response.encoding = "gbk"
        tree = etree.HTML(response.text)
        li_list = tree.xpath('//ul[@class="clearfix"]/li')  # 获取列表页每一条数据
        # 请求列表页---》列表页取出每一个详情页的url----》请求详情页---》取出大图的下载链接
        for li in li_list:
            detail_url = li.xpath('./a/@href')[0]  # 取出详情页的url
            image_name = li.xpath('./a/b/text()')[0]  # 图片名字
            # 图片名字不能包含特殊符号 *
            image_name = image_name.replace('*','')
            detail_url  = "https://pic.netbian.com"+detail_url
            # print(image_name,detail_url)
            # 请求详情页 https://pic.netbian.com/tupian/34737.html
            detail_response = requests.get(url=detail_url,headers=headers1)
            detail_response.encoding ="gbk"
            detail_tree =  etree.HTML(detail_response.text) # 解析详情页的响应
            image_url = detail_tree.xpath('//a[@id="img"]/img/@src')[0]
            image_url = "https://pic.netbian.com"+image_url
            # print(image_url)
            save_img(image_name,image_url)
def save_img(image_name,image_url):
    # 4： 保存到本地
    # print(image_name,image_url)
    image_content = requests.get(url=image_url,headers=headers1).content # 获取二进制的响应数据
    # 图片名字 就用我们解析的image_name 图片后缀不能落下
    with open(f'./images/{image_name}.jpg','wb')as f:
        f.write(image_content) # 把图片的响应写入到文件
        print(f'========={image_name}下载成功============')

main()
