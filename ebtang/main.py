__author__ = 'linliang'

from scrapy.crawler import CrawlerProcess
from douban_movie.spiders.douban import DoubanSpider
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(DoubanSpider)
    process.start()  # the script will block here until the crawling is finished
