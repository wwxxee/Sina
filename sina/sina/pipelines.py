# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class SinaPipeline(object):
    def __init__(self, host, user, password, database,port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port


    def process_item(self, item, spider):
        sql = "insert into HuiYiZhuanYongXiaoMaJia (fid, screen_name, profile_image_url, profile_url, followers_count, follow_count, desc1) values (%s,%s,%s,%s,%s,%s,%s);"
        self.cursor.execute(sql, [item['fid'], item['screen_name'], item['profile_image_url'], item['profile_url'], item['followers_count'], item['follow_count'], item['desc1']])
        self.conn.commit()

        return item


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self,spider):
        """
        当Spider开启时，这个方法被调用
        :param spider: Spider 的实例
        :return:
        """
        self.conn = pymysql.connect(
            host =self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        """
        当Spider关闭时，这个方法被调用
        :param spider:
        :return:
        """
        self.cursor.close()
        self.conn.close()

class Qingxi(object):
    def process_item(self, item, spider):
        item['fid'] = item['fid'][0]
        item['screen_name'] = item['screen_name'][0]
        item['profile_image_url'] = item['profile_image_url'][0]
        item['profile_url'] = item['profile_url'][0]
        item['followers_count'] = item['followers_count'][0]
        item['follow_count'] = item['follow_count'][0]
        item['desc1'] = item['desc1'][0]

        return item