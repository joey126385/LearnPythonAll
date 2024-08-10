'''
        mysql  python
        python代码爬取数据 要存到MySQL数据
        python 和MySQL的交互 pymysql python里去操作MySQL的一个库
        pip install pymysql

'''
import pymysql

# pymysql 操作MySQL
# 1： 连接MySQL
connect = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="spidercode")
cursor = connect.cursor() # 创建游标对象 帮我们做sql语句的一些
cursor.execute("select * from demo") # 数据查找
# cursor.execute("insert into demo(name,age) values ('西风',19999)") # 数据查找
# connect.commit() #确认提交 数据才会存MySQL
print(cursor.fetchall())


cursor.close() #  关闭游标
connect.close() # 关闭连接
