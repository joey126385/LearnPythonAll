'''
    这个页面的招标信息 只要爬这个页面就行 注意目标url的查找 爬10页 存到Excel 单表
    思路分析
        1： 寻找目标url
            http://www.ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do
            post请求  载荷里面都是参数
            目的是爬10页 要找每一页的链接  page代表页数
        2： 发起请求 获取响应
        3： json解析数据
        4：调用Excel模板 保存到Excel
'''
import json
import requests
import os, xlwt, xlrd
from xlutils.copy import copy
def SaveExcel(data):
    os_mkdir_path = os.getcwd() + '/数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '数据.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""      # 设置表名
        worksheet1 = workbook.add_sheet("采购网", cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ("id","编号","省份","时间","类型","标题")
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
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# https://www.toolhelper.cn/Url/UrlParameterJson 快速生成键值对参数
for page in  range(1,11):
    data1 = {
        "nType": "prcmNotices",
        "pType": "",
        "prcmPrjName": "",
        "prcmItemCode": "",
        "prcmOrgName": "",
        "startDate": "2023-08-09",
        "endDate": "2024-08-07",
        "prcmPlanNo": "",
        "page": page,
        "pageSize": 18
    }
    print(f'===========当前是第{page}页=========')
    url1=  "http://www.ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do"
    response =requests.post(url=url1,headers=headers1,data= data1)

    res_data = json.loads(response.text) # 响应的数据 转python格式

    for data in res_data['rows']: # 循环取出每一条数据
        AREA_NAME = data['AREA_NAME'] # 省份
        NEWWORK_DATE = data['NEWWORK_DATE'] # 时间
        NOTICE_NAME = data['NOTICE_NAME'] # 类型
        NOTICE_TITLE = data['NOTICE_TITLE'] # 标题
        ORG_CODE = data['ORG_CODE'] # id
        if "PRCM_PLAN_NO" not in data: # 判断一下有没有这个key 没有设置默认值
            number = "空值"
        else:
            number = data['PRCM_PLAN_NO'] # 编号
        datas = {
            "采购网":[ORG_CODE,number,AREA_NAME,NEWWORK_DATE,NOTICE_NAME,NOTICE_TITLE]
        }

        print(datas)
        SaveExcel(datas) # 注意传参




