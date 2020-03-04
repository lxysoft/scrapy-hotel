# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YilonghotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 地址
    addr = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 价格
    blance = scrapy.Field()
    # 分数
    score = scrapy.Field()
    # 评论数
    evaluation = scrapy.Field()
    # pass
