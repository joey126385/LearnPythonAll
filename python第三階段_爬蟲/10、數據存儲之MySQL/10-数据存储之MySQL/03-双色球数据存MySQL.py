'''
    需求
        爬取双色球开奖数据 (一等奖。。。字段)存到MySQL
    分析思路
    函数写法
        1：目标url
            https://datachart.500.com/ssq/history/history.shtml
            GET请求
        2： 发起请求 获取响应
        3： xpath对字段做数据的提取
        4：保存到MySQL

'''
import pymysql
import requests
from lxml import etree


def save_mysql(data):
    # 保存到mysql中
    #  # 1： 连接MySQL
    connect = pymysql.connect(host="localhost", port=3306, user="root", password="root", db="spidercode")
    cursor = connect.cursor()  # 创建游标对象 帮我们做sql语句的一些操作
    try:
        sql = "insert into doubule_demo values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        cursor.execute(sql)
    except Exception:
        connect.rollback()  # 不保存
        print("sql语句出现问题请检查")
        # 可以把报错的sql语句存到文件里 方便我们后续排查
    else:
        connect.commit()  # 没问题 正常提交
    cursor.close()
    connect.close()

def main():
    # 代码开始方法
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    url1 = "https://datachart.500.com/ssq/history/history.shtml"
    response = requests.get(url=url1, headers=headers1)
    response.encoding = "gb2312"
    tree = etree.HTML(response.text)
    tr_list = tree.xpath('//tr[@class="t_tr1"]')
    # print(tr_list)
    for tr in tr_list:  # 循环解析每一条数据
        number = tr.xpath('./td[1]/text()')[0]  # 期号
        blue_ball = tr.xpath('./td[8]/text()')[0]  # 蓝球
        prize_pool = tr.xpath('./td[10]/text()')[0]  # 奖池奖金
        all_prize = tr.xpath('./td[15]/text()')[0]  # 总投注金额
        draw_date = tr.xpath('./td[16]/text()')[0]  # 开奖日期
        first_prize = '-'.join(tr.xpath('./td[11]/text() | ./td[12]/text() '))  # 一等奖
        two_prize = '-'.join(tr.xpath('./td[13]/text() | ./td[14]/text() '))  # 二等奖
        red_ball = '-'.join(tr.xpath('./td[@class="t_cfont2"]/text()'))  # 匹配红球号码
        # print(number,blue_ball,prize_pool,all_prize,draw_date,first_prize,two_prize,red_ball)
        data = [number, blue_ball, prize_pool, all_prize, draw_date, first_prize, two_prize, red_ball]
        save_mysql(data)


main()  # 调用方法
