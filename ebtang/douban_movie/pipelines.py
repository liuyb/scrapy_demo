# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from twisted.enterprise import adbapi
from scrapy.pipelines.images import ImagesPipeline
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        return d

        #self.dbpool.runOperation(
        #    'INSERT INTO directory(`ebtang_id`, `title`, `date`, `crawl_time`) VALUES (%s,%s,%s,%s)',
        #    (item['ebtang_id'], item['title'], item['date'], item['crawl_time']))

    def _do_upinsert(self, conn, item, spider):
        conn.execute("select * from directory where ebtang_id = %s", (item['ebtang_id'], ))
        result = conn.fetchone()
        if result:
            #telegram_send.send('湘西赶尸鬼事更新了：' + item['title']);
            pass
        else:
            self.dbpool.runOperation(
                'INSERT INTO directory(`ebtang_id`, `title`, `date`, `crawl_time`) VALUES (%s,%s,%s,%s)',
                (item['ebtang_id'], item['title'], item['date'], item['crawl_time']))
            tips = '%s%s%s' % ('proxychains4 telegram-send "湘西赶尸鬼事更新了:', item['title'], '"');
            os.system(tips)
        return item


class MovieImagesPipeline(ImagesPipeline):
    DEFAULT_IMAGES_RESULT_FIELD = 'picture_path'

    #def get_media_requests(self, item, info):
    #   return Request(item['picture'])

