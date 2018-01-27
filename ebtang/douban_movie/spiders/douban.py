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
            'Referer': 'https://www.douban.com'
            }
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/top250',
    )

    rules = (
        Rule(LinkExtractor(allow=(r"https://movie\.douban\.com/top250\?start=\d+&filter=")),
             callback='parse_item'),
    )

    def parse_item(self, response):
        for item in response.xpath('//div[@id="content"]/div/div[1]/ol/li'):
            l = DoubanMovieItemLoader(DoubanMovieItem(), item)
            l.add_xpath('rank', './div/div/em/text()')
            l.add_xpath('picture', './div/div/a/img/@src')
            l.add_xpath('title', './div/div/div/a/span/text()')
            l.add_xpath('info', './div/div/div/p/text()')
            l.add_css('star', 'div.star span.rating_num::text')
            l.add_xpath('people', './div/div/div/div/span[4]/text()')
            l.add_css('quote', 'p.quote > span.inq::text')
            l.add_value('crawl_time', datetime.now())
            yield l.load_item()

    def parse_start_url(self, response):
        return self.parse_item(response)
