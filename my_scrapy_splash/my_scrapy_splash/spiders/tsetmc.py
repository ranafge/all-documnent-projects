import scrapy
from scrapy_splash import SplashRequest

class TsetmcSpider(scrapy.Spider):
    name = 'tsetmc'
    allowed_domains = ['tsetmc.com']
    # start_urls = ['http://tsetmc.com/']

    def start_requests(self):
        yield SplashRequest(
            url = 'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=42354736493447489',
            callback=self.parse,args={'wait': 10}
        )

    def parse(self, response):
        print(response.status)
        print(response.css('div.box2.zi1').extract())
        for td in response.css('div.box2.zi1').xpath('//table'):
            print(td)
        # print(response.body.decode("utf-8")) # deconde for original format.





