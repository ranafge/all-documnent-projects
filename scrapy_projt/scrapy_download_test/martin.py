import scrapy

from scrapy.http import Request

class CollegesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
class CollegesSpider(scrapy.Spider):
    name = 'colleges'
    allowed_domains = ["4icu.org"]
    start_urls = ('http://www.4icu.org/in/',)

    def parse(self, response):
        for tr in response.xpath('//div[@class="section group"] [5]/div[@class="col span_2_of_2"][1]/table//tr'):
            if tr.xpath(".//td[@class='i']"):
                item = CollegesItem()
                item['name'] = tr.xpath('./td[1]/a/text()').extract()[0]
                item['location'] = tr.xpath('./td[2]//text()').extract()[0]
                yield item
