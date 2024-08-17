'''
    需求
        爬取梨视频一页的视频 下载到本地
        异步加载： 页面局部刷新 往下拉动滚动条 加载出新的数据 数据的响应在XHR类型的请求里面、
    1：如果我们需要生成 多个url(这个url就是每次请求拿到对应更新的数据)
        需要 找到每一个url不一样的地方 跟前面的翻页的流程一样
        分析发现 每次加载的url start依次递增24
        https://www.pearvideo.com/panorama_loading.jsp?start={} 依次递增24 列表页
        for page in range(0,241,24): 爬10页的for循环
            print(page)
    2： 视频 是在详情页看到的
        去详情页找到视频的下载链接 爬多个视频 需要找到每一个视频的下载链接
        https://video.pearvideo.com/mp4/short/20240810/cont-1795772-16034656-hd.mp4 视频的播放链接
        https://video.pearvideo.com/mp4/short/20240810/cont-1795770-16034648-hd.mp4 视频的播放链接
        https://video.pearvideo.com/mp4/short/20240810/cont-1795769-16034644-hd.mp4
        2.1： cont—视频的ID 这个ID在详情页URL地址栏里面就包含了 怎么获取每一个详情页的视频ID 列表页跳转到详情页
        所以说 列表页他就有所有详情页的url  可以在列表取出所有视频详情页的ID
        2.2：16034656 第二个变化的地方
        XHR 请求找到一个像视频下载链接的
            https://www.pearvideo.com/videoStatus.jsp?contId=1795709&mrd=0.6502616997014843
            https://www.pearvideo.com/videoStatus.jsp?contId=1795769&mrd=0.17940641798409063

        虚假的下载链接 访问不了
        https://video.pearvideo.com/mp4/short/20240810/1723464227597-16034644-hd.mp4 XHR响应的url
        https://video.pearvideo.com/mp4/short/20240810/1723464181793-16034648-hd.mp4 2
        https://video.pearvideo.com/mp4/short/20240807/1723465158980-16034404-hd.mp4  3
        真的能访问
        https://video.pearvideo.com/mp4/short/20240810/cont-1795769-16034644-hd.mp4 视频的下载链接
        https://video.pearvideo.com/mp4/short/20240810/cont-1795770-16034648-hd.mp4 2
        https://video.pearvideo.com/mp4/short/20240807/cont-1795709-16034404-hd.mp4  3

        ！！！这里写的XHR代表包含了虚假下载链接的url！！！
        假的和真的 哪里不一样？  1723464227597 cont-1795769 其他的地方都是一样的
        我们现在拿到的是假的下载链接    我们通过分析规律是生成不了每一个视频的真实的下载链接的
        因为 视频第二处(2.2)变化的地方不能通过规律生成  只能找一个这个值在哪个请求的响应里面有
        ！！！为啥要去请求包含了虚假视频下载链接的XHR请求： 因为他里面包含了第二处变化地方的值！！！
        搜索发现 XHR请求中 有一个虚假的下载链接 包含了这个变化的点
        现在： 可以取出XHR里面这个假的下载链接 他和真的只有一处不一样 ===》 1723464227597 cont-1795769
            不一样的地方 就是把 1723464227597 变成cont-id 就可以了
        得到真实的下载链接 就可以保存到本地

    实现的步骤
        1： 访问列表页url
            https://www.pearvideo.com/panorama_loading.jsp?start={}
        2： 从列表页的响应 取出每一个视频的ID
        3：拿到ID  去请求详情页中的XHR请求(里面包含了虚假的下载链接)
        4： 从XHR的响应中 获取得到虚假的下载链接
        5:  对虚假的下载链接做一个替换  1723464227597变成cont-id 就可以得到真实的下载链接
        6： 文件操作保存到本地
'''
import re
import requests
from lxml import etree
import json
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
def main():
    # 1： 访问列表页url
    url1 = "https://www.pearvideo.com/panorama_loading.jsp?start=0"
    response = requests.get(url=url1, headers=headers1)
    tree = etree.HTML(response.text)
    # 如果以后 元素面板的xpath能匹配到 本地匹配不到 数据 就先打印响应 看看响应有没有我们要的数据(确定有木有请求成功)
    # 看一下 本地响应的内容 和浏览器网络面板这个url的层级结构  看看是不是和元素面板有区别 有区别 以本地的响应为准
    # 响应的内容 和页面看到的不一样
    li_list = tree.xpath('//li[@class="categoryem"]')
    # 2： 从列表页的响应 取出每一个视频的ID
    for li in li_list:
        video_id = li.xpath('./div/a/@href')[0]  # # video_1795788
        video_id = video_id.split('_')[1]  # 以我们指定的字符分割  分割成列表
        video_title = li.xpath('./div/a/div[@class="vervideo-title"]/text()')[0]  # 视频标题
        video_title = re.sub('[\\\\/:*?\"<>|]', '', video_title)
        #  3：拿到ID  去请求详情页中的XHR请求(里面包含了虚假的下载链接)
        # https://www.pearvideo.com/videoStatus.jsp?contId=1795709&mrd=0.6502616997014843
        # print(video_id,video_title)
        headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Referer": f"https://www.pearvideo.com/video_{video_id}"  # 页面跳转来源字段
        }
        # 经过测试 请求videoStatus需要携带Referer 不然会失败
        detail_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={video_id}"
        detail_response = requests.get(url=detail_url, headers=headers2)
        # print(detail_response.text)
        # 4： 从XHR的响应中 获取得到虚假的下载链接
        detail_res =  json.loads(detail_response.text) # json转python
        video_false_url = detail_res['videoInfo']['videos']['srcUrl'] # 虚假的下载链接
        # 5:  对虚假的下载链接做一个替换  1723464227597变成cont-id 就可以得到真实的下载链接
        new_false_url = video_false_url.split('/')[-1] #  '1723468592639-16034732-hd.mp4'
        new_false_url = new_false_url.split('-')[0] # 1723468646689
        video_url = video_false_url.replace(new_false_url,f"cont-{video_id}") # 虚假的下载链接 替换成真的
        # print(video_url)
        save_video(video_url,video_title) # 函数调用 传给保存方法
def save_video(video_url,video_title):
    # 6： 文件操作保存到本地
    image_content = requests.get(url=video_url,headers=headers1).content # 获取二进制的响应数据
    with open(f'./video/{video_title}.mp4','wb')as f:
        f.write(image_content) # 把图片的响应写入到文件
        print(f'========={video_title}下载成功============')
main()
