import os
import time
import xlrd
import xlwt

import requests
from lxml import etree
from xlutils.copy import copy

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def SaveExcels(data, index):
    # 获取表的名称
    sheet_name = [i for i in data.keys()][0]
    # 创建保存excel表格的文件夹
    # os.getcwd() 获取当前文件路径
    os_mkdir_path = os.getcwd() + '/数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '贝壳多表数据.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""  # 设置表名
        worksheet1 = workbook.add_sheet(index, cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ( '房屋标题', '房屋地址', '房屋标签','房屋来源','价格')
        # 将表头写入工作簿
        for header_num in range(0, len(sheet1_headers)):
            # 设置表格长度
            worksheet1.col(header_num).width = 2560 * 3
            # 写入表头        行,    列,           内容
            worksheet1.write(0, header_num, sheet1_headers[header_num])
        # 循环结束，代表表头写入完成，保存工作簿
        workbook.save(os_excel_path)
    """=============================已有工作簿添加新表==============================================="""
    # 打开工作薄
    workbook = xlrd.open_workbook(os_excel_path)
    # 获取工作薄中所有表的名称
    sheets_list = workbook.sheet_names()
    # 如果表名称：字典的key值不在工作簿的表名列表中
    if sheet_name not in sheets_list:
        # 复制先有工作簿对象
        work = copy(workbook)
        # 通过复制过来的工作簿对象，创建新表  -- 保留原有表结构
        sh = work.add_sheet(sheet_name)
        # 给新表设置表头
        excel_headers_tuple = ( '房屋标题', '房屋地址', '房屋标签','房屋来源','价格')
        for head_num in range(0, len(excel_headers_tuple)):
            sh.col(head_num).width = 2560 * 3
            #               行，列，  内容，            样式
            sh.write(0, head_num, excel_headers_tuple[head_num])
        work.save(os_excel_path)
    """========================================================================================="""
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


for page in range(1, 101):
    response = requests.get(url="https://cc.zu.ke.com/zufang", headers=headers1)
    tree = etree.HTML(response.text)
    print(f'=========第{page}页开始爬取===========')
    div_list = tree.xpath('//div[@class="content__list--item"]')
    print(len(div_list))
    for div in div_list:
        title = div.xpath('.//div[@class="content__list--item--main"]/p[1]/a/text()')[0].strip()  # 标题
        detail = div.xpath('.//div[@class="content__list--item--main"]/p[2]//text()')  # 房屋详情
        label = div.xpath('.//div[@class="content__list--item--main"]/p[3]//text()')  # 房屋标签
        source = div.xpath('.//div[@class="content__list--item--main"]/p[4]//text()')  # 房屋来源
        price = div.xpath(
            './/div[@class="content__list--item--main"]/span[@class="content__list--item-price"]//text()')  # 房屋详情
        detail1 = ''.join(detail).replace(' ', '').replace('\n', '')
        label1 = ''.join(label).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        source1 = ''.join(source).replace(' ', '').replace('\n', '')  # 列表拼接成字符串 然后把空格和换行替换成空
        price1 = ''.join(price)
        index = f"贝壳第{page}页"  # 爬第一页的时候   index = 贝壳第1页 爬第二页的时候   index = 贝壳第2页
        data = {
            # 表名肯定是不一样的
            index: [title, detail1, label1, source1, price1]
        }
        print(data)
        SaveExcels(data,index)
        # print(title,detail1,label1, source1, price1)
    time.sleep(2)  # 强制停止2秒
    print(f'=========第{page}页爬取完毕===========')
