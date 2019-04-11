# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors


class LianjiaInfoPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='lianjia',  # 数据库名
            user='root',  # 数据库用户名
            passwd='xn990112..',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into house_info
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",  # python操作mysql
            (item['lianjia_id'], item['name'], item['district'], item['house_address'],
             item['total_price'], item['unit_price'], item['build_area'],
             item['inner_area'], item['decoretion'], item['house_type'], item['elevator'],
             item['face'], item['floors'], item['house_structure'],
             item['build_age'], item['ownership'], item['view_time'],
             item['build_type'], item['build_structure'], item['EH_ratio'],
             item['listing_time'], item['last_trsx'], item['property_age_limit'],
             item['housing_purposes'], item['property_owned'], item['mortgage_info'],
             item['premises_permit'], item['house_age_limit'], item['community_aver_price'],
             item['subway_site'], item['subway_distance'], item['favorite_count'], item['view_month_count'],
             item['view_count']
             ))
        self.connect.commit()  # 提交sql语句
        return item  # 必须实现返回
