"""
     搜索栏输入任意关键字 爬对应的数据 爬10页存数据库 不用爬详细内容
    爬虫步骤
        1： 明确目标url
            https://kns.cnki.net/kns8s/brief/grid post请求
            data参数比较多 pageNum 代表的就是页数
        2： 发起请求 获取响应
        3： 数据解析 xpath
        4: 存到MySQL
"""
import time

import pymysql
import requests
from lxml import etree

headers1 = {
    "Referer": "https://kns.cnki.net/kns8s/defaultresult/index",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def main():
    for page in range(1, 11):
        url1 = "https://kns.cnki.net/kns8s/brief/grid"
        data1 = {
            # true 第一页为true  后面的页数都是false
            "boolSearch": "false",
            "QueryJson": "{\"Platform\":\"\",\"Resource\":\"CROSSDB\",\"Classid\":\"WD0FTY92\",\"Products\":\"\",\"QNode\":{\"QGroup\":[{\"Key\":\"Subject\",\"Title\":\"\",\"Logic\":0,\"Items\":[{\"Field\":\"SU\",\"Value\":\"python\",\"Operator\":\"TOPRANK\",\"Logic\":0,\"Title\":\"主题\"}],\"ChildItems\":[]}]},\"ExScope\":1,\"SearchType\":2,\"Rlang\":\"CHINESE\",\"KuaKuCode\":\"YSTT4HG0,LSTPFY1C,JUP3MUPD,MPMFIG1A,EMRPGLPA,WQ0UVIAA,BLZOG7CK,PWFIRAGL,NN3FJMUV,NLBO1Z6R\",\"SearchFrom\":1}",
            "pageNum": f"{page}",
            "pageSize": "20",
            "sortField": "",
            "sortType": "",
            "dstyle": "listmode",
            "boolSortSearch": "false",
            "productStr": "YSTT4HG0,LSTPFY1C,RMJLXHZ3,JQIRZIYA,JUP3MUPD,1UR4K4HZ,BPBAFJ5S,R79MZMCB,MPMFIG1A,EMRPGLPA,J708GVCE,ML4DRIDX,WQ0UVIAA,NB3BWEHK,XVLO76FD,HR1YT1Z9,BLZOG7CK,PWFIRAGL,NN3FJMUV,NLBO1Z6R,",
            "aside": "主题：python",
            "searchFrom": "资源范围：总库",
            "CurPage": "1"}
        response = requests.post(url=url1, headers=headers1, data=data1)
        # print(response.text)
        parser_html(response.text)  # 函数调用 把响应的内容传给parser_html 他用res接收
        # print('================')
        time.sleep(2)


# 方法里面的代码  方法不调用 是不会被直接
def parser_html(res):
    # 负责解析html的数据 需要一个的内容 才能对其做解析
    # print(res)
    tree = etree.HTML(res)
    tr_list = tree.xpath('//tbody/tr')
    for tr in tr_list:
        seq = ''.join(tr.xpath('.//td[@class="seq"]/text()')).strip() # 序号
        title = ''.join(tr.xpath('.//td[@class="name"]/a//text()')) # 标题
        author = '-'.join(tr.xpath('.//td[@class="author"]/a/text()')) # 作者
        source = ''.join(tr.xpath('.//td[@class="source"]/p/a/text()')) # 来源
        date = ''.join(tr.xpath('.//td[@class="date"]/text()')) # 发布时间
        data = ''.join(tr.xpath('.//td[@class="data"]/span/text()')) # 数据库
        sql_data = [seq,title,author,source,date,data]
        print(sql_data)
        save_mysql(sql_data)
def save_mysql(sql_data):
    # 把数据保存到MySQL
    #  # 1： 连接MySQL
    connect = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="spidercode")
    cursor = connect.cursor()  # 创建游标对象 帮我们做sql语句的一些操作
    try:
        sql = "insert into zhiwang values ('%s','%s','%s','%s','%s','%s')" % (
        sql_data[0], sql_data[1], sql_data[2], sql_data[3], sql_data[4], sql_data[5])
        cursor.execute(sql)
    except Exception:
        connect.rollback()  # 不保存
        print("sql语句出现问题请检查")
        # 可以把报错的sql语句存到文件里 方便我们后续排查
    else:
        connect.commit()  # 没问题 正常提交
    cursor.close()
    connect.close()

main()
