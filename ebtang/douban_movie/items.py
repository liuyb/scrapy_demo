# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose


class DoubanMovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ebtang_id = Field()
    title = Field()
    date = Field()
    crawl_time = Field()


class GetPeopleNum(object):

    def __call__(self, values):
        return values[0][:-3]


class DoubanMovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    # 去掉'636840人评价'中的'人评价'
    people_in = GetPeopleNum()
    # 或者
    # people_in = Compose(lambda values: values[0][:-3])
    info_out = Compose(TakeFirst(), lambda info: info.strip())
