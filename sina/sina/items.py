# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fid = scrapy.Field()
    screen_name = scrapy.Field()
    profile_image_url = scrapy.Field()
    profile_url = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    desc1 = scrapy.Field()

