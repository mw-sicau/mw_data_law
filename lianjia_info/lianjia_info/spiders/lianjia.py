# -*- coding: utf-8 -*-
import scrapy
from re import search
from selenium import webdriver
from lianjia_info.items import LianjiaInfoItem
from selenium.webdriver.chrome.options import Options



class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['cd.lianjia.com']

    def __init__(self):

        chrome_options = Options()
        chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.set_page_load_timeout(30)

        self.Err_count = 0
        self.house_count = 0
        self.page_count = 0

    def closed(self, spider):
        self.browser.close()
        print('Chrome关闭')

    def start_requests(self):

        urls = ['https://cd.lianjia.com/ershoufang/pg%d/' % i for i in range(1,101)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面提交给parse方法处理

    def parse(self, response):
        self.page_count += 1
        house_detail_urls = response.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/@href').extract()

        for url in house_detail_urls:
            yield scrapy.Request(url=url, callback=self.parse_detail)
        # 继续下一页 有问题
        # next_page = response.xpath('//*[@id="content"]/div[1]/div[8]/div[2]/div/a[5]/@href').extract_first()
        # print(next_page)
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        self.house_count += 1
        print('正在爬取第：%d页，第：%d条数据，错误：%d条' %
              (self.page_count, self.house_count, self.Err_count))
        try:
            name = response.xpath(
                '/html/body/div[5]/div[2]/div[4]/div[1]/a[1]/text()').extract_first()  # 小区名称
            district = response.xpath(
                '/html/body/div[5]/div[2]/div[4]/div[2]/span[2]/a[1]/text()').extract_first()  # 行政区划
            house_address = response.xpath(
                '/html/body/div[4]/div/div/a/text()').extract()[1:]
            house_address = ''.join(house_address).replace('二手房', '')  # 地址
            total_price = response.xpath(
                '/html/body/div[5]/div[2]/div[2]/span[1]/text()').extract_first()  # 总价
            unit_price = response.xpath(
                '/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/span/text()').extract_first()  # 每平米单价
            build_area = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').extract_first()  # 建筑面积
            inner_area = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract_first()  # 套内面积
            decoretion = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract_first()  # 装修情况
            house_type = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').extract_first()  # 住房类型
            elevator = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract_first()  # 配备电梯
            face = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract_first()  # 房屋朝向
            floors = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').extract_first()  # 所在楼层
            house_structure = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').extract_first()  # 房屋结构
            build_age = response.xpath(
                '//*[@id="resblockCardContainer"]/div/div/div[2]/div/div[2]/span/text()').extract_first()  # 修建时间
            ownership = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[2]/span[2]/text()').extract_first()  # 交易权属
            view_time = response.xpath(
                '/html/body/div[5]/div[2]/div[4]/div[3]/span[2]/text()').extract_first()  # 看房时间
            lianjia_id = response.xpath(
                '/html/body/div[5]/div[2]/div[4]/div[4]/span[2]/text()').extract_first()  # 链家编号
            build_type = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract_first()  # 建筑类型
            build_structure = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[8]/text()').extract_first()  # 建筑结构
            EH_ratio = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').extract_first()  # 梯户比例
            listing_time = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract_first()  # 挂牌时间
            last_trsx = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()').extract_first()  # 上次交易
            property_age_limit = response.xpath(
                '//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').extract_first()  # 产权年限
            housing_purposes = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').extract_first()  # 房屋用途
            property_owned = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()').extract_first()  # 产权所属
            mortgage_info = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[7]/span[2]/text()').extract_first().strip()  # 抵押信息
            premises_permit = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[8]/span[2]/text()').extract_first()  # 房本备件
            house_age_limit = response.xpath(
                '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[5]/span[2]/text()').extract_first()  # 房屋年限
            community_aver_price = response.xpath(
                '//*[@id="resblockCardContainer"]/div/div/div[2]/div/div[1]/span/text()').extract_first()  # 小区均价
            favorite_count = response.xpath(
                '//*[@id="favCount"]/text()').extract_first()#关注人数
            view_month_count = response.xpath(
                '//*[@id="record"]/div[2]/div[3]/span/text()').extract_first()#月看房数
            view_count = response.xpath(
                '//*[@id="cartCount"]/text()').extract_first()#总看房数
            try:
                subway_line = response.xpath(
                    '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]/text()').extract_first()  # 地铁线路
                subway_site = response.xpath(
                    '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]/text()').extract_first()  # 地铁站点
                subway_site = subway_line + subway_site
                subway_distance = response.xpath(
                    '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]/text()').extract_first()  # 距地铁站直线距离
                subway_distance = search(r'\d+', subway_distance).group()
            except:
                subway_site = None
                subway_distance = None

            if build_area != '暂无数据':
                build_area = search(r'\d+\.?\d*', build_area).group()
            else:
                build_area = None
            if inner_area != '暂无数据':
                inner_area = search(r'\d+\.?\d*', inner_area).group()
            else:
                inner_area = None
            if property_age_limit != '暂无数据':
                property_age_limit = search(r'\d+\.?\d*', property_age_limit).group()
            else:
                property_age_limit = None
            if community_aver_price != '暂无数据':
                community_aver_price = search(r'\d+', community_aver_price).group()
            else:
                community_aver_price = None
            if last_trsx == '暂无数据':
                last_trsx = None

            item = LianjiaInfoItem()
            item['name'] = name
            item['district'] = district
            item['house_address'] = house_address
            item['total_price'] = total_price
            item['unit_price'] = unit_price
            item['build_area'] = build_area
            item['inner_area'] = inner_area
            item['decoretion'] = decoretion
            item['house_type'] = house_type
            item['elevator'] = elevator
            item['face'] = face
            item['floors'] = floors
            item['house_structure'] = house_structure
            item['build_age'] = build_age
            item['ownership'] = ownership
            item['view_time'] = view_time
            item['lianjia_id'] = lianjia_id
            item['build_type'] = build_type
            item['build_structure'] = build_structure
            item['EH_ratio'] = EH_ratio
            item['listing_time'] = listing_time
            item['last_trsx'] = last_trsx
            item['property_age_limit'] = property_age_limit
            item['housing_purposes'] = housing_purposes
            item['property_owned'] = property_owned
            item['mortgage_info'] = mortgage_info
            item['premises_permit'] = premises_permit
            item['house_age_limit'] = house_age_limit
            item['community_aver_price'] = community_aver_price
            item['subway_site'] = subway_site
            item['subway_distance'] = subway_distance
            item['favorite_count'] = favorite_count
            item['view_month_count'] = view_month_count
            item['view_count'] = view_count
            yield item
        except:
            self.Err_count += 1
