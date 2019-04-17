# from scrapy import cmdline
#
# cmdline.execute('scrapy crawl lianjia'.split())

import pymysql
from openpyxl import Workbook

connect = pymysql.connect(
    host='127.0.0.1',  # 数据库地址
    port=3306,  # 数据库端口
    db='lianjia',  # 数据库名
    user='root',  # 数据库用户名
    passwd='479803313',  # 数据库密码
    charset='utf8',  # 编码方式
    use_unicode=True)
# 通过cursor执行增删查改
cursor = connect.cursor()
cursor.execute()

