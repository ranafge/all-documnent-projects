import json
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "quotes-infinite-scroll"
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        data = json.loads(response.text)
        print('\n', data, '\n')
        for quote in data['quotes']:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags'],
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)


# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     },
# })
#
# process.crawl(QuotesInfiniteScrollSpider)
# process.start() # the script will block here until the crawling is finished
