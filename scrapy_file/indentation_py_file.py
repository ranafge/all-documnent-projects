from scrapy.spiders.crawl import CrawlSpider
import json
import scrapy

class CiencuadraSpider(CrawlSpider):
    name = "Ciencuadras"
    item_count = 0
    allowed_domain = ['www.ciencuadras.com']

    start_urls = ['https://www.ciencuadras.com/venta',]#'https://www.ciencuadras.com/arriendo',]

    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent':self.user_agent})
    
    def parse(self, response):
        json_response = json.loads(response.xpath('//script[@id="ciencuadras-state"]/text()').get())
        yield {'x': json_response}
