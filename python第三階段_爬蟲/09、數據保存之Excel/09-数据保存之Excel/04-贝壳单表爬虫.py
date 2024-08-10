'''
    爬取长春1页租房数据保存到Excel
    思路
        1： 目标url
            https://cc.zu.ke.com/zufang
        2： 发起请求获取响应
        3：数据解析 xpath
        4：使用模板代码 保存到本地
'''
import os, xlwt, xlrd
from xlutils.copy import copy
import time
from lxml import etree
import requests
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def SaveExcel(data):
    os_mkdir_path = os.getcwd() + '/数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '贝壳.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""      # 设置表名
        worksheet1 = workbook.add_sheet("贝壳租房数据", cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ( '房屋标题', '房屋地址', '房屋标签','房屋来源','价格')
        # 将表头写入工作簿
        for header_num in range(0, len(sheet1_headers)):
            # 设置表格长度
            worksheet1.col(header_num).width = 2560 * 3
            # 写入            行, 列,           内容
            worksheet1.write(0, header_num, sheet1_headers[header_num])
        # 循环结束，代表表头写入完成，保存工作簿
        workbook.save(os_excel_path)

    # 判断工作簿是否存在
    if os.path.exists(os_excel_path):
        # 打开工作簿
        workbook = xlrd.open_workbook(os_excel_path)
        # 获取工作薄中所有表的个数
        sheets = workbook.sheet_names()
        for i in range(len(sheets)):
            for name in data.keys():
                worksheet = workbook.sheet_by_name(sheets[i])
                # 获取工作薄中所有表中的表名与数据名对比
                if worksheet.name == name:
                    # 获取表中已存在的行数
                    rows_old = worksheet.nrows
                    # 将xlrd对象拷贝转化为xlwt对象
                    new_workbook = copy(workbook)
                    # 获取转化后的工作薄中的第i张表
                    new_worksheet = new_workbook.get_sheet(i)
                    for num in range(0, len(data[name])):
                        new_worksheet.write(rows_old, num, data[name][num])
                    new_workbook.save(os_excel_path)
for page in range(1,11):

    response =requests.get(url="https://cc.zu.ke.com/zufang",headers=headers1)
    tree = etree.HTML(response.text)
    print(f'=========第{page}页开始爬取===========')
    div_list = tree.xpath('//div[@class="content__list--item"]')
    print(len(div_list))
    for div in div_list:
        title = div.xpath('.//div[@class="content__list--item--main"]/p[1]/a/text()')[0].strip()  # 标题
        detail = div.xpath('.//div[@class="content__list--item--main"]/p[2]//text()')  # 房屋详情
        label = div.xpath('.//div[@class="content__list--item--main"]/p[3]//text()')  # 房屋标签
        source = div.xpath('.//div[@class="content__list--item--main"]/p[4]//text()')  # 房屋来源
        price = div.xpath('.//div[@class="content__list--item--main"]/span[@class="content__list--item-price"]//text()')  # 房屋详情
        detail1 = ''.join(detail).replace(' ', '').replace('\n', '')
        label1 = ''.join(label).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        source1 = ''.join(source).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        price1 = ''.join(price)
        # print(title,detail1,label1, source1, price1)
        data = {
            "贝壳租房数据":[title,detail1,label1, source1, price1]
        }
        print(data)
        SaveExcel(data) #循环中调用 循环一次 就是一条数据 调用方法 保存到Excel

    time.sleep(2)  # 强制停止2秒
    print(f'=========第{page}页爬取完毕===========')

