from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
# from tutorial2.items import Tutorial2Item

class QuotesSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]'), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        for items in response.xpath('//div[@class="quote"]'):

            l = ItemLoader(item=Tutorial2Item(),selector=items)
            l.add_xpath('text','span[@class="text"]/text()')
            l.add_xpath('author','span/small[@class="author"]/text()')
            l.add_xpath('author_link','span/a/@href')
            l.add_xpath('tags','div[@class="tags"]/a[@class="tag"]/text()')
            l.add_xpath('tags_link','div[@class="tags"]/a[@class="tag"]/@href')

            yield l.load_item()

