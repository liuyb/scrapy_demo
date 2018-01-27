# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from twisted.enterprise import adbapi
from scrapy.pipelines.images import ImagesPipeline


class MySQLPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        dbapi_name = settings.get('DB_API_NAME')
        dbargs = settings.get('DB_ARGS')
        dbpool = adbapi.ConnectionPool(dbapi_name, **dbargs)
        return cls(dbpool)

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runOperation(
            'INSERT INTO top250(rank, picture, title, info, star, quote, people, crawl_time) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)',
            (item['rank'], item['picture'], item['title'], item['info'], item['star'],
             item.get('quote', ''),
             item['people'], item['crawl_time']))
        return item


class MovieImagesPipeline(ImagesPipeline):
    DEFAULT_IMAGES_RESULT_FIELD = 'picture_path'

    def get_media_requests(self, item, info):
        return Request(item['picture'])
