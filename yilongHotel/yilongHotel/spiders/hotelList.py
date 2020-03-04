# -*- coding: utf-8 -*-
import scrapy
from yilongHotel.items import YilonghotelItem
from scrapy.http import Request


class HotellistSpider(scrapy.Spider):
    name = 'hotelList'
    allowed_domains = ['elong.com']
    start_urls = ['http://hotel.elong.com/search/list_cn_101.html?pageIndex=1']
    custom_settings = {
        "headers": {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Cookie': 'CookieGuid=158948cd-563a-4211-8a3e-a92bd263cba0; page_time=1509628060819%2C1509628152402%2C1509628219681%2C1509693907739%2C1509693938986%2C1509693967862%2C1509701358453%2C1509701412108%2C1509764088450%2C1509764288344%2C1509772980043%2C1509773457586%2C1509773753700%2C1509774349211%2C1509774650832%2C1509775873404%2C1509775901516%2C1509776293716%2C1509776386781%2C1509776424331%2C1509776587625%2C1509776889277%2C1509778200633%2C1509779461446; _RF1=111.225.131.187; _RSG=zs4ixjEH93BfifEVp1.6NB; _RDG=28df89f13e8f75279825ba18abc6dd550e; _RGUID=b0c944eb-7bb0-4dbd-b5c6-f81cdf3a9b29; ShHotel=CityID=0101&CityNameCN=%E5%8C%97%E4%BA%AC%E5%B8%82&CityName=%E5%8C%97%E4%BA%AC%E5%B8%82&OutDate=2017-11-06&CityNameEN=beijing&InDate=2017-11-05; _fid=j9jp7iwv-bf9b-4c1d-8c4f-893b780f205c; newjava1=a79d58d364ea53c8c9161ec3b2f45c8d; JSESSIONID=EB741B472421B3E455397D577D009DE8; SessionGuid=6a99e379-6ae4-4a74-b0a4-f94dfe60ab5a; Esid=1ec4caeb-c805-4d96-8ddf-43a6a23eed52; com.eLong.CommonService.OrderFromCookieInfo=Status=1&Orderfromtype=1&Isusefparam=0&Pkid=50&Parentid=50000&Coefficient=0.0&Makecomefrom=0&Cookiesdays=0&Savecookies=0&Priority=8000; fv=pcweb; s_cc=true; s_sq=%5B%5BB%5D%5D; s_visit=1',
            'Host': 'hotel.elong.com ',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '1062'
        },
    }

    def parse(self, response):
        item = YilonghotelItem()
        hote_count = response.xpath("//span[@id='hotelCount']/text()").extract()[0]
        item["score"] = response.xpath("//i[@class='t20 c37e']/text()").extract()
        item["blance"] = response.xpath("//span[@class='h_pri_num ']/text()").extract()
        item["title"] = response.xpath("//span[@class='info_cn']/text()").extract()
        item["link"] = response.xpath("//span[@class='info_cn']/@data-link").extract()
        addr = response.xpath("//p[@class='h_info_b2']/text()").extract()
        item["addr"] = addr[1:len(addr):3]
        item["evaluation"] = response.xpath("//span[@class='c555 block mt5']/b/text()").extract()
        yield item
        page_count = int(hote_count) // 20 + 1
        for i in range(2, 2):
            yield Request('http://hotel.elong.com/search/list_cn_101.html?pageIndex=' + str(i),
                          callback=self.parse)
