# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import DoubanMovieItem
from douban_movie.items import DoubanMovieItemLoader
from datetime import datetime


class DoubanSpider(CrawlSpider):
    name = "douban"
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Referer': 'https://www.ebtang.com'
            }
    allowed_domains = ["www.ebtang.com"]
    start_urls = (
        'http://www.ebtang.com/book/246/directory',
    )

    #rules = (
    #    Rule(LinkExtractor(allow=(r"https://movie\.douban\.com/top250\?start=\d+&filter=")),
    #         callback='parse_item'),
    #)

    def parse_item(self, response):
        for item in response.xpath('//div[@class="body-bg"]/div[@class="w1000"]/div/div/ul/li'):
            l = DoubanMovieItemLoader(DoubanMovieItem(), item)
            l.add_xpath('ebtang_id', './a/@href')
            l.add_xpath('title', './a/text()')
            l.add_xpath('date', './span/text()')
            l.add_value('crawl_time', datetime.now())
            yield l.load_item()

    def parse_start_url(self, response):
        return self.parse_item(response)
