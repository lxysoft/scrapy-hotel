# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class YilonghotelPipeline(object):
    def process_item(self, item, spider):
        title = item["title"]
        addr = item["addr"]
        link = item["link"]
        blance = item["blance"]
        score = item["score"]
        evaluation = item["evaluation"]
        for i in range(0, len(title)):
            print("--------------------------------------------------------")
            print("名称:%s  价格:%s   分数：%s  评论数：%s " % (title[i], blance[i], score[i], evaluation[i]))
            print("地址:%s         详情链接:%s" % (addr[i].replace("\n", "", 3), "http://hotel.elong.com"+link[i]))

        return item
