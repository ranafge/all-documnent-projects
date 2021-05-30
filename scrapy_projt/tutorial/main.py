import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import cmdline
cmdline.execute("scrapy crawl articleItems".split())
