# -*- coding: utf-8 -*-
import scrapy
import json
import jsonpath
from sina.items import SinaItem


class FansSpider(scrapy.Spider):
    name = 'fans'
    allowed_domains = ['m.weibo.cn']
    #  博主url
    url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3217179555&since_id="
    offset = 1
    start_urls = [url+str(offset),]

    def parse(self, response):
        result = json.loads(response.text)
        cardgroup = jsonpath.jsonpath(result,"$..card_group")[0] # jsonpath返回一个列表
        for fan in cardgroup:
            # type(fan) --> dict
            item = SinaItem()
            item['fid'] = jsonpath.jsonpath(fan, "$..id")
            item['screen_name'] = jsonpath.jsonpath(fan, "$..screen_name")
            item['profile_image_url'] = jsonpath.jsonpath(fan, "$..profile_image_url")
            item['profile_url'] = jsonpath.jsonpath(fan, "$..profile_url")
            item['followers_count'] = jsonpath.jsonpath(fan, "$..followers_count")
            item['follow_count'] = jsonpath.jsonpath(fan, "$..follow_count")
            item['desc1'] = jsonpath.jsonpath(fan, "$..desc1")
            yield item

        self.offset += 1
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)



