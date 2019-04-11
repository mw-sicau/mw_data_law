# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    district = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    build_area = scrapy.Field()
    inner_area = scrapy.Field()
    decoretion = scrapy.Field()
    house_type = scrapy.Field()
    elevator = scrapy.Field()
    face = scrapy.Field()
    floors = scrapy.Field()
    house_structure = scrapy.Field()
    build_age = scrapy.Field()
    ownership = scrapy.Field()
    view_time = scrapy.Field()
    lianjia_id = scrapy.Field()
    build_type = scrapy.Field()
    build_structure = scrapy.Field()
    EH_ratio = scrapy.Field()
    listing_time = scrapy.Field()
    last_trsx= scrapy.Field()
    property_age_limit = scrapy.Field()
    housing_purposes = scrapy.Field()
    property_owned = scrapy.Field()
    mortgage_info = scrapy.Field()
    premises_permit = scrapy.Field()
    house_age_limit = scrapy.Field()
    house_address = scrapy.Field()
    community_aver_price =scrapy.Field()
    subway_site = scrapy.Field()
    subway_distance = scrapy.Field()
    favorite_count = scrapy.Field()
    view_month_count = scrapy.Field()
    view_count = scrapy.Field()
