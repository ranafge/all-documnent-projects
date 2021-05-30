import scrapy
from scrapy.utils.response import open_in_browser
from urllib.parse import urljoin
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from ..items import Article
from scrapy.crawler import CrawlerProcess
from scrapy import Request
from selenium import webdriver
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader

class ArticleSpider(CrawlSpider):
   name = 'articleItems'
   allowed_domains = ['wikipedia.org']
   start_urls = ['https://en.wikipedia.org/wiki/Benevolent'
              '_dictator_for_life']
   rules = [Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
         callback='parse_items', follow=True)]

   def parse_items(self, response):
      article = {}
      article['url'] = response.url
      article['title'] = response.css('h1::text').extract_first()
      article['text'] = response.xpath('//div[@id='
                                     '"mw-content-text"]//text()').extract()

      lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
      article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
      return article


import scrapy
import json
class BasisMembersSpider(scrapy.Spider):
    name = 'basis'
    allowed_domains = ['basis.org.bd']

    def start_requests(self):

        yield scrapy.Request(url="https://basis.org.bd/get-member-list?page=1&team=", callback=self.get_membership_no)


    def get_membership_no(self, response):

        data_array = json.loads(response.body)['data']

        for data in data_array:

            yield scrapy.Request(url='https://basis.org.bd/get-company-profile/{0}'.format(data['membership_no']), callback=self.parse)


    def parse(self, response):
        print("I want to get this line on console. thank you.")


import scrapy
from bs4 import BeautifulSoup

class PostscrapeItem(scrapy.Item):
    full_text = scrapy.Field()


class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.scrapinghub.com/page/1/'
    ]

    def parse(self, response):
        so = BeautifulSoup(response.text, 'html.parser')
        item = PostscrapeItem()

        if so.find('em'):
            concatenated = ""
            text_samples = so.find_all('em')

            for t_s in text_samples:
                concatenated += t_s.text

            item['full_text'] = concatenated

        return item



class PreopenMarketDataSpider(scrapy.Spider):

    name = 'preopen_market_data'
    allowed_domains = ['www1.nseindia.com']
    start_urls = ['https://www1.nseindia.com/live_market/dynaContent/live_watch/pre_open_market/pre_open_market.htm']

    def parse(self, response):
        stocks = ['RELIANCE', 'TATASTEEL', 'LT']
        for stock in stocks:
            stock_url  = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/pre_open/preOpenOrderBook.jsp?param='+stock+'EQN&symbol='+stock
            yield Request(stock_url, callback=self.data)

    def data(self,response):
        p=response.xpath('//*[@class="orderBookFontCBig"]/text()').extract()
        # print(p)
        yield Request(p,callback=self,meta={'Stock':p})

class YCSpider(scrapy.Spider):
    name = "ycspider"

    def start_requests(self):
        urls = [
            'https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice',
            'https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'ycblog-{page}.html'
        print(filename, '\n')
        parsedText = response.xpath('//p').getall()
        print('\n', parsedText, '\n')
        with open(filename, 'w') as f:
            for x in parsedText:
                f.write(x)
        self.log(f'Saved file {filename}')


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
        print('x\n')
        json_response = response.xpath('//script[@id="ciencuadras-state"]/text()').get()
        yield {'x': json_response}


class mySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ['https://www.phoenixcontact.com/online/portal/gb?1dmy&urile=wcm%3apath%3a/gben/web/main/products/subcategory_pages/Tools_P-25/3d7b966e-fe2c-4aab-ad5f-b98db236d62a']
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,headers=self.headers,callback=self.parse)

    def parse(self,response):
        soup = BeautifulSoup(response.text,"lxml")
        if soup.select_one("div:has(> h3:contains('Category')) > ul > li > a"):
            for item in soup.select("div:has(> h3:contains('Category')) > ul > li > a"):
                item_link = response.urljoin(item.get("href"))
                yield scrapy.Request(item_link,headers=self.headers,callback=self.parse,dont_filter=True)

        elif soup.select_one("h1:contains('Product list')"):
            yield scrapy.Request(response.url,headers=self.headers,callback=self.parse_content,dont_filter=True)


    def parse_content(self,response):
        soup = BeautifulSoup(response.text,"lxml")
        for item in soup.select("[class='pxc-sales-data-wrp'][data-product-key] h3 > a[href][onclick]"):
            print(item.get_text(strip=True))

        next_page = soup.select_one("a.pxc-pager-next")
        if next_page:
            base_url = soup.select_one("base").get("href")
            next_page_link = urljoin(base_url,next_page.get("href"))
            print("*****************",next_page_link)
            yield scrapy.Request(next_page_link,headers=self.headers,callback=self.parse_content)


import scrapy
from scrapy.exceptions import CloseSpider


class ProdutosSpider(scrapy.Spider):
    name = 'produtos_aplus'
    allowed_domains = ['www.allpartsnet.com.br']
    start_urls = ["https://www.allpartsnet.com.br/buscapagina?fq=B%3a1228&O=OrderByNameASC&PS=50&sl=5d58b484-137e-4091-92ca-29d2e0c70f85&cc=1&sm=0&PageNumber=0"]
    page = 0

    def parse(self, response):
        print("\n\n in parse", response.url, "\n\n")

        if len(response.xpath("//h3[@class='shelf-product-name ']/a/@href")) == 0:
            raise CloseSpider('No more products to scrape...')

        for produtos in response.xpath("//div[@class='QD prateleira row qd-xs n1colunas']/ul"):

            link = produtos.xpath(".//h3[@class='shelf-product-name ']/a/@href").get()
            cod_all = produtos.xpath(".//span[@class='insert-sku-name']/text()").get()


            yield response.follow(url=link, callback=self.parse_produto, meta={'link': link, 'cod_all': cod_all})


        self.page += 1
        yield scrapy.Request(
            url=f'https://www.allpartsnet.com.br/buscapagina?fq=B%3a1228&O=OrderByNameASC&PS=50&sl=5d58b484-137e-4091-92ca-29d2e0c70f85&cc=1&sm=0&PageNumber={self.page}',
            callback=self.parse
        )


    def parse_produto(self, response):
        link = response.request.meta['link']
        cod_all = response.request.meta['cod_all']
        for produtos in response.xpath("//div[@class='vehicle-selection']/div[@id='caracteristicas']"):
            yield{

                'link': link,
                'cod_all': cod_all,
                'fabricante': produtos.xpath(".//td[@class='value-field Fabricante']/text()").get(),
                'ean': produtos.xpath(".//td[@class='value-field Codigo-EAN']/text()").get(),
                'oem': produtos.xpath(".//td[@class='value-field Codigo-OEM']/text()").get()

            }

import scrapy

# from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/page/1/']
    def parse(self, response):
        count_of_quote =0
        number_of_quote = 0
        count_of_quote += int(float(response.xpath("count(//div[@class='quote'])").extract()[0].strip())) # count method
        number_of_quote += count_of_quote

        items = {}
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            # title = quotes.css('span.text::text').extract()
            # author = quotes.css('.author::text').extract()
            # tags = quotes.css('.tag::text').extract()
            items['url'] = response.url
            # items['title'] = title
            # items['author'] = author
            # items['tags'] = tags
            items['count_of_quote'] = count_of_quote
            yield items
        print(number_of_quote)
        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) + '/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            # print('\n', response.follow(next_page), '\n')
            yield response.follow(next_page, callback = self.parse)


import scrapy

class PartSpider(scrapy.Spider):
    name = 'part_spider'
    start_urls = ['https://parts.cat.com/AjaxCATPartLookupResultsView?catalogId=10051&langId=-1&requestType=1&storeId=21801&serialNumber=KSN00190&keyword=&link=']

    def parse(self, response):
        SET_SELECTOR = 'table.partlookup_table'
        data = []
        for part in response.css(SET_SELECTOR):
            name= part.css('span.resPartName  a::text').extract()
            data.append(name)
            partnumber= part.css('span.resPartNum a::text').extract()
            data.append(partnumber)
            print(data)

class LeadHomeSpider(scrapy.Spider):
    name = "lead_home"
    allowed_domain = ['www.leadhome.co.za']
    start_urls = [
        'https://www.leadhome.co.za/search/property-for-sale/western-cape/4?sort=date',
    ]

    # parse search page
    def parse(self, response):
        print('\n', response.url, '\n')
        # follow property link
        offering = 'buy' if 'sale' in response.css('h1::text').get() else 'rent'
        print('\n', offering, '\n')
        for prop in response.css('div.search__PropertyCardWrapper-sc-1j5dndx-0.bsqBpI'):
            print('\n prop ', prop )
            link = 'https://www.leadhome.co.za' + prop.css('a::attr(href)').get()
            print('\n lin in prop ', link, '\n')
            a = prop.css('p.styles__Label-h53xsw-16.bcSkCI::text').getall()
            print('\na', a, '\n')
            #prop_type = attempt_get_property_type(a[0]) if len(a) != 0 else None
            area = a[1] if len(a) > 1 else None
            print('\n', link, '\n')
            yield scrapy.Request(
                link,
                meta={'item': {
                    'agency': self.name,
                    'url': link,
                    'area': area,
                    'offering': offering,
                    #'property_type': prop_type,
                }},
                callback=self.parse_property,
            )

        # follow to next page
        next_page_number = response.xpath(
            '//a[contains(@class, "styles__PageNumber-zln67a-0 jRCKhp")]/following-sibling::a/text()').get()
        if next_page_number is not None:
            new_page_link = 'https://www.leadhome.co.za/search/property-for-sale/western-cape/4?sort=date&page=' + next_page_number
            next_page = response.urljoin(new_page_link)
            print('\n', next_page, '\n')
            yield scrapy.Request(next_page, callback=self.parse)

    # parse property
    def parse_property(self, response):
        print('*'*10)
        items = {}
        items['myitem'] = response.meta.get('item')
        items['parking'] = response.xpath('//p[contains(text(), "Uncovered Parking:")]/following-sibling::p/text()').get()
        yield items

class MainSpider(scrapy.Spider):
    name = 'main'
    directory = 'https://www.constructionenquirer.com/directory'
    start_urls = [directory]

    def parse(self, response):
        sectors = response.xpath('(//select[@name="sector"]/option)[position()>1]')
        for sector in sectors:
            vals = sector.xpath('.//@value').get()
            print('\n', vals, '\n')

            data = {
                'ce-directory-action': 'sector-search',
                'sector': vals,
                'action': 'find-firms-by-sector'
            }

            yield scrapy.FormRequest(url=self.directory, formdata=data, callback=self.parse_sectors)

    def parse_sectors(self, response):
        print('\n', response.url, '\n')
        yield {
            "Name": response.xpath('//h3/a/text()').get()
        }

import scrapy

class LinksSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['daraz.com.bd']
    extracted_links = []
    shop_list = []

    def start_requests(self):
        start_urls = 'https://www.daraz.com.bd'
        yield scrapy.Request(url=start_urls, callback=self.extract_link)

    def extract_link(self, response):
        str_response_content_type = str(response.headers.get('content-type'))
        if str_response_content_type == "b'text/html; charset=utf-8'" :
            links = response.xpath("//a/@href").extract()
            for link in links:
                link = link.lstrip("/")
                if ("https://" or "http://") not in link:
                    link = "https://" + str(link)

                split_link = link.split('.')

                if "daraz.com.bd" in link and link not in self.extracted_links:
                    self.extracted_links.append(link)
                    if len(split_link) > 1:
                        if "www" in link and "daraz" in split_link[1]:
                            yield scrapy.Request(url=link, callback=self.extract_link, dont_filter=True)
                        elif "www" not in link and "daraz" in split_link[0]:
                            yield scrapy.Request(url=link, callback=self.extract_link, dont_filter=True)

                        if "daraz.com.bd/shop/" in link and link not in self.shop_list:
                            yield {
                                "links" : link
                            }


import scrapy
class ZalandoWomenSpider(scrapy.Spider):
    name = 'zalando_women_historic_2015'
    allowed_domains = ['www.web.archive.org']
    base_url = ['https://web.archive.org/web/20150906222155mp_/https://www.zalando.co.uk/womens-clothing/']
    star_urls = base_url + ['https://web.archive.org/web/20150630111618/https://www.zalando.co.uk/womens-clothing/?p={0}'.format(x) for x in range(2,3)]

    custom_settings = {
        "DOWNLOAD_DELAY": 10,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
        "handle_httpstatus_list" : 403
    }

    def start_requests(self):
        for url in self.star_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        print('\n')
        print(response.url)
        products = response.css("u.catalogArticlesList.threeCol.main")
        print('here')
        print(products)
        for data in products:
            print(data.css('a.catalogArticlesList_content::attr("href")'))
            print(data.css('div.catalogArticlesList_priceBox'))
            print(data.css('div.catalogArticlesList_articleName'))

import scrapy
import pandas
from scrapy.http import FormRequest
from lxml.html import fromstring
from scrapy.crawler import CrawlerProcess

class WikiCityScraperOG(scrapy.Spider):
    name = 'WikiCityScraperOG'
    def start_requests(self):
        urls=["https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        test = response.xpath('//title/text()').extract()
        test2 = response.xpath('//a[@href="/wiki/List_of_United_States_urban_areas"]/text()').extract()
        test3 = response.xpath('//a[@href="/wiki/list_of_United_States_urban_areas"]/@title')
        test4 = response.xpath('//a[@href="/wiki/list_of_United_States_urban_areas"]/@title').extract()
        test5 = response.xpath('/html/@class')
        test6 = response.xpath('/html/@class').extract()
        print(test)
        print(test2)
        print(test3)
        print(test4)
        print(test5)
        print(test6)

class QuotesSpider(CrawlSpider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/login',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'test@test.com',
            'password' : 'test'
        }, callback=self.scrap_content)

    def scrap_content(self, response):
        #open_in_browser(response) Apenas para testar se o login funcionou.

        items = {}

        quotes_div = response.css('div.quote')


        page = response.url.split("/")[-2]

        tags = ['misattributed-to-einstein']

        for quote in quotes_div:
            if quote.css('.tag::text').get() in tags:
                text = quote.css('span.text::text').extract()
                author = quote.css('.author::text').extract()
                tag = quote.css('.tag::text').extract()

                items['text'] = text
                items['author'] = author
                items['tag'] = tag
                items['page'] = page
                yield items

            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback= self.scrap_content)

import scrapy

class ActScraper1Spider(scrapy.Spider):
    name = 'act_scraper_1'
    allowed_domains = ['sso.agc.gov.sg']
    start_urls = ['https://sso.agc.gov.sg/Act/AA2004']

    def parse(self, response):
        info = response.xpath("//*[@id='tocNav']")
        titles = info.xpath("//li/a/span/text()").getall()
        # all title
        # for title in titles:
        #     print(title.strip())
        for i in info:

                yield {
                    'short title': i.xpath('//*[@id="toc"]/li[4]/ul/li[1]/a/span/text()').get().strip(),
                    'Interpretation title2': i.xpath('//*[@id="toc"]/li[4]/ul/li[2]/a/span/text()').get().strip(),
                    'Administration of Act title2': i.xpath('//*[@id="toc"]/li[5]/ul/li[1]/a/span/text()').get().strip(),
                }

import scrapy
from selenium import webdriver
class MovieSpider(scrapy.Spider):
    name = "movies"
    start_urls = ["https://www.thetoptens.com/animals/"]
    def __init__(self):
        self.driver = webdriver.Chrome()
    def parse(self, response):
        nextFlag = True
        self.driver.get(self.start_urls[0])
        while nextFlag:
            next_page = self.driver.find_element_by_xpath("//div[@class='pages']/a[@class='g' and text()=9]")
            if next_page:
                a = response.xpath("//div[@class='listgrid']/a/text()").getall()
                yield {
                    "aaa": a
                 }
                next_page.click()
            else:
                nextFlag = False
        self.driver.close()
import scrapy

class PerfumesSpider(scrapy.Spider):
    name = 'perfumes'
    allowed_domains = ['www.fragrancenet.com']
    start_urls = ['https://www.fragrancenet.com/fragrances']
    custom_settings = {"DOWNLOADER_MIDDLEWARES": {'tutorial.middlewares.RandomUserAgentMiddleware': 400,
                                                      'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}}


    def parse(self, response):
        for perfumes in response.xpath("//div[@id='resultSet']"):

            #nome = perfumes.xpath(".//span[@class='brand-name']/text()").get(),
            link = perfumes.xpath(".//p[@class='desc']/a/@href").get()

            yield response.follow(url=link, callback=self.parse_produto, meta={'link' : link})

        next_page = response.xpath("//a[@data-rel='next']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_produto(self, response):
        link = response.request.meta['link']
        for produto in response.xpath("//div[@class='topZone cf']"):

            yield{
            'link': link,
            'gender': produto.xpath(".//span[@class='genderBar desktop']/span/span/text()").get(),
            'name': produto.xpath(".//span[@class='productTitle']/text()").get(),
            'year': produto.xpath(".//ul[@class='notes cf']/li[3]/span[2]/text()").get(),
            'brand': produto.xpath("normalize-space(.//p[@class='uDesigner']/a/text())").get(),
            'size': produto.xpath(".//span[@class='sr-only']/text()").getall(),
            'price': produto.xpath(".//div[@class='pricing']/text()").getall(),
            'discount': produto.xpath(".//div[@class='fnet-offer']/a/span/span/text()").get(),
            }


import scrapy
import requests
import json

class ExampleSpider(scrapy.Spider):
    name = 'examplee'
    allowed_domains = []
    start_urls = ['https://prd-usta-kube.clubspark.io/unified-search-api/api/Search/tournaments/Query?indexSchema=tournament']

    def get_headers(self):
        headers={
                'content-type': 'application/json;charset=UTF-8',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        return headers
    def get_payload(self):
        payload={"options":{"size":100,"from":0,"sortKey":"distance","latitude":40.41553497314453,"longitude":-82.70935821533203},"filters":[{"key":"organisation-id","items":[]},{"key":"location-id","items":[]},{"key":"region-id","items":[]},{"key":"publish-target","items":[{"value":1}]},{"key":"level-category","items":[{"value":"junior"}],"operator":"Or"},{"key":"date-range","items":[{"minDate":"2021-01-01T00:00:00.000Z","maxDate":"2021-01-31T18:29:59.999Z"}],"operator":"Or"},{"key":"event-division-gender","items":[],"operator":"Or"},{"key":"event-division-age-category","items":[],"operator":"Or"},{"key":"organisation-group","items":[],"operator":"Or"},{"key":"distance","items":[],"operator":"Or"},{"key":"tournament-level","items":[],"operator":"Or"},{"key":"event-ntrp-rating-level","items":[],"operator":"Or"},{"key":"event-division-event-type","items":[],"operator":"Or"},{"key":"event-court-location","items":[],"operator":"Or"}]}
        return payload

    def page_resp(self,response):
        url='https://prd-usta-kube.clubspark.io/unified-search-api/api/Search/tournaments/Query?indexSchema=tournament'
        response = requests.post(url, headers=self.get_headers,json=self.get_payload)
        sample=response.json()
        print(sample)


import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = [
    'https://perfumehut.com.pk/shop/',
]

    def parse(self, response):

            yield {
                    'product_link': response.css('a.product-image-link::attr("href")').get(),
                    'product_title': response.css('h3.product-title>a::text').get(),
                    'product_price': response.css('span.price > span > bdi::text').get(),

                }
            next_page = response.css('ul.page-numbers>li>a.next.page-numbers::attr("href")').get()

            if next_page is not None:
                print()
                print(next_page)
                print()
                yield scrapy.Request(next_page)

            # if next_page is not None:
            #     yield scrapy.Request(url=next_page)
            # print(nex_page)
        # yield {
        # 'title': response.css('h1::text').get(),
        # 'batt': response.css('td.woocommerce-product-attributes-item__value p::text')[3].get(),
        # 'brand': response.css('div.woodmart-product-brand img::attr(alt)').get(),
        # 'brandimg': response.css('div.woodmart-product-brand img::attr(src)').get(),
        # 'price': response.css('p.price').xpath('./span/bdi/text()').get(),
        # 'r-price': response.css('p.price').xpath('./del/span/bdi/text()').get(),
        # 's-sale': response.css('p.price').xpath('./ins/span/bdi/text()').get(),
        # 'breadcrumbs': response.css('nav.woocommerce-breadcrumb a::text').getall(),
        # 'tags': response.css('span.tagged_as a::text').getall(),
        # 'attributes': response.css('td.woocommerce-product-attributes-item__value p::text').getall(),
        # 'img': response.css('figure.woocommerce-product-gallery__image a::attr("href")').getall(),
        # 'description': response.css('div.woocommerce-product-details__short-description p::text').get(),
        # 'description1': response.css('#tab-description > div > div > p::text').getall(),
        # 'description2': response.css('#tab-description > div > div > div > div > div > div > div > div > p::text').getall()
        # }
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def parse(self, response):
        for boat in response.css('div#product-list.productList'):
            yield {
                'url': boat.css('div.col-6-12.mobile-col-1-1.envItem>article.boatAd.js-boatAd::attr("data-product-url")').getall(),
                'boat_title': boat.css('div.col-6-12.mobile-col-1-1.envItem>article.boatAd.js-boatAd::attr("data-title")').getall(),
                'boat_model': boat.css('div.col-6-12.mobile-col-1-1.envItem>article.boatAd.js-boatAd::attr("data-model")').getall(),
                'boat_type': boat.css('div.col-6-12.mobile-col-1-1.envItem>article.boatAd.js-boatAd::attr("data-type-boat")').getall(),
            }


import scrapy
# from fundrazr.items import FundrazrItem
from datetime import datetime
import re


class Fundrazr(scrapy.Spider):
    name = "my_scraper"
    start_urls = ["https://perfumehut.com.pk/shop/page/{}/".format(x) for x in range(1, 59)]
    custom_settings = {
        "download_delay": 5,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)


    def parse(self, response):
        for href in response.xpath("//h3[contains(@class, 'product-title')]/a/@href"):
            # add the scheme, eg http://
            url  = "" + href.extract()

            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = {}

        # Getting Campaign Title
        item['campaignTitle'] = response.xpath("//h1[contains(@class, 'entry-title')]/text()").extract()

        yield item

        # for item in response.css(".product-grid-item"):
        #     yield {
        #         'product_link': item.css('a.product-image-link::attr("href")').get(),
        #         'product_title': item.css('h3.product-title > a::text').get(),
        #         'product_price': item.css('span.price > span > bdi::text').get(),
        #     }
        #     break

LUA_SCRIPT = """
function main(splash)
    splash.private_mode_enabled = false
    splash:go(splash.args.url)
    splash:wait(2)
    html = splash:html()
    splash.private_mode_enabled = true
    return html
end
"""
class ProductSpider(scrapy.Spider):

    name = "product"

    def start_requests(self):
        urls = [
            "https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/drug-tariff"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_1)

    def parse_1(self, response):
        lst_url = response.css("a.ckbtn::attr(href)").extract()
        print(lst_url[0])
        yield SplashRequest(url=lst_url[0],
                            endpoint='execute',
                            callback=self.parse_online_doc,
                            args={
                            'wait':10,
                            "lua_source":LUA_SCRIPT
                        })

    def parse_online_doc(self, response):
        print(response.url)
        result = response.css("li.TOPL-DC00794839.bm_topic hasChildren childrenVisible active").extract()
        print('Results...')
        print(result) # here I see an empty list

import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
import time

class ActSpider(scrapy.Spider):
    name = 'ACT'
    allowed_domains = ['sso.agc.gov.sg']
    start_urls = [
        'https://sso.agc.gov.sg/Act/AA2004'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        chrome_path = which('chromedriver')

        driver =  webdriver.Chrome(executable_path=chrome_path,  options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://sso.agc.gov.sg/Act/AA2004")

        #insert scroller function?

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=str(self.html))
        for table in resp.xpath("//div[@class='body']"):
            yield {
                'info': table.xpath('./table/text()').getall()
            }
import scrapy

class My_spider(scrapy.Spider):
    name= "book_crawler"

    def start_requests(self):
        url_list=[]
        for i in range(2 , 5):
            url_list.append("https://books.toscrape.com/catalogue/page-" + str(i) + ".html")
        urls=[]
        urls.append("https://books.toscrape.com/")
        for i in range(0 , len(url_list)):
            urls.append(url_list[i])

        for url in urls:
            yield scrapy.Request(url= url, callback= self.parse)


    def parse(self,response):
        title_list = response.css("ol.row").xpath('//h3/a/text()').extract()
        print(title_list)
        with open('../../book_titel.txt', 'a+') as f:
            for i in range(0, len(title_list)) :
                f.write(str(i)+ " : " + title_list[i] + "\n")


class HtSpider(scrapy.Spider):
    name = 'sells'
    custom_settings = {
        "COOKIES_ENABLED" : True,
        "COOKIES_DEBUG" : False

    }
    allow_domain = ['hattrick.org']

    def start_requests(self):
        urls = ['https://www.hattrick.org']
        for url in urls:
            player = 'goto.ashx?path=/Club/Players/Player.aspx?playerId=450940600'
            joint = urljoin(url, player)
            print(' \n', joint, '\n')
            yield scrapy.Request(
                url=joint,
                # cookies={'currency': 'USD', 'country': 'UY'},
                cookies=[{'name': 'currency', "country": 'US', 'value': 'USD','domain': 'hattrick.org'}],
                # cookies={'currency': 'USD', 'country': 'US'},
                # meta={'dont_merge_cookies': True},
                meta={'currency': 'USD', 'country': 'YU'},
                dont_filter=True,callback=self.price)

    def price(self,response):
        cookie = response.headers.getlist('Set-Cookie')[0]#.split(";")#[0].split("=")
        print(cookie)
        price_xpath = response.xpath('//* [@id="transferHistory"]/table//tr[1]/td[6]/text()').extract_first()
        print(response.meta['currency'])
        print(response.meta['country'])
        print(price_xpath) # it is not in USD but in Riel :(
    # open_in_browser(response) # to check if it is in Riel or in USD

# from ..items import REItem
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

class RealEstateSpider(scrapy.Spider):
    name = 'realestates'
    start_urls = [
        'www.webtoscrape.com'
    ]

    def parse(self, response):
        item_loader = ItemLoader(response=response)
        item_loader.default_input_processor = MapCompose(remove_tags)
        item_loader.default_output_processor = TakeFirst()

        item_loader.add_css("price", ".offer-item-price")
        item_loader.add_css("size", ".offer-item-area")
        item_loader.add_css("rooms", ".offer-item-rooms")

        yield item_loader.load_item()


        next_page = response.css('.pager-next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from appinformatica.items import appinformaticaItem

import w3lib.html


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ParserSpider(CrawlSpider):
    name = 'parser'
    allowed_domains = ['eksisozluk.com']
    start_urls = ['https://eksisozluk.com/basliklar/gundem']

    rules = (
        Rule((LinkExtractor(
            restrict_xpaths="//ul[@class='topic-list']/li/a")), callback='parse_item', follow=True, ),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[@id='title']/a/text()").getall(),
            'entry': response.xpath("//div[@class='content']/text()").getall(),
            'yazar': response.xpath("//a[@class='entry-author']/text()").getall(),
            'title': response.xpath("//a[@class='entry-date permalink']/text()").getall(),

        }



import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from appinformatica.items import appinformaticaItem

import w3lib.html

class appinformaticaSpider (CrawlSpider):
    name = 'appinformatica'
    # allowed_domains = ["appinformatica.com"]
    item_count=0
    start_urls =['https://www.appinformatica.com/telefonos/moviles/']
    rules = {
        Rule(LinkExtractor(allow=(r'/moviles/.*\.html'), ),
             callback='parse_item', follow=True)
    }

    def parse_item(self, response):
        item = {}
        self.item_count += 1
        item['Modelo'] = w3lib.html.remove_tags(response.xpath("//h1").get(default=''))
        item['Position'] = self.item_count
        item['Precio'] = w3lib.html.remove_tags(response.xpath('//*[@id="ficha-producto"]/div[2]/div[1]/div/div[1]').get(default=''))
        item['PrecioTienda'] = w3lib.html.remove_tags(response.xpath('//*[@id="ficha-producto"]/div[2]/div[1]/div/div[2]').get(default=''))
        item['Stock'] = w3lib.html.remove_tags(response.xpath('//*[@id="ficha-producto"]/div[2]/div[3]/p[3]').get(default=''))
        item['Submodelo'] = w3lib.html.remove_tags(response.xpath('//*[@id="ficha-producto"]/div[2]/div[3]/p[2]/strong[2]').get(default=''))
        item['Url'] = w3lib.html.remove_tags(response.url)
        yield item

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ParserSpider(CrawlSpider):
    name = 'parser'
    allowed_domains = ['eksisozluk.com']
    start_urls = ['https://eksisozluk.com/']

    rules = (
        Rule((LinkExtractor( allow=(r'/.*a=popular(?:&p=\d+)?'))), callback='parse_item', follow=True, ),
        # Rule((LinkExtractor( allow=r'.*popular&p=\d+')), callback='parse_item', follow=True, ),

    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[@id='title']/a/span/text()").getall(),
            'entry': response.xpath("//div[@class='content']/text()").getall(),
            'yazar': response.xpath("//a[@class='entry-author']/text()").getall(),
            'date': response.xpath("//a[@class='entry-date permalink']/text()").getall(),

        }

        # next_page = response.xpath("//a[@class='next']/@href").get()

        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)

        # next_page_url = response.xpath(
        #     "//a[@class='next']/@href").get()

import scrapy
class StarbucksSpider(scrapy.Spider):
    name = 'starbucks'
    allowed_domains = ['gameflip.com/shop/gift-cards/starbucks']
    start_urls = ['https://gameflip.com/shop/gift-cards/starbucks?limit=36&platform=starbucks&accept_currency=USD&status=onsale']

    def parse(self, response):

        slots = response.xpath('//*[@class="listing-detail view-grid col-6 col-md-4 col-lg-3 col-xl-2"]')

        for slot in slots:

            fullPrice = slot.xpath('.//*[@class="col-12 description normal"]/text()').extract_first()
            Discount = slot.xpath('.//*[@class="badge badge-success listing-discount"]/text()').extract_first()
            price = slot.xpath('.//*[@class="money"]/text()').extract_first()
            status = slot.xpath('.//*[@alt="sold"]/@alt').extract_first()

            print ('\n')
            print (status)
            print (fullPrice)
            print (Discount)
            print (price)
            print ('\n')

            next_PageUrl = response.css('url.pager > li[2] > a.btn::attr("href")').extract_first()
            print('NEXT PAGE URL', next_PageUrl)
            absoulute_next_page_url = response.urljoin(next_PageUrl)
            print('\n absoulite url ')
            print(absoulute_next_page_url)
            print('\n ')
            yield scrapy.Request(absoulute_next_page_url)


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class item(scrapy.Item):
    field1 = scrapy.Field()
    field2 = scrapy.Field()

class GenericSpider(scrapy.Spider):

    name = "Generic"

    def __init__(self, *args, **kwargs):
        input = kwargs.get('urls', '').split(',') or []
        self.start_urls = []
        self.allowed_domains = []
        for url in input:
            self.allowed_domains.append(url)
            self.start_urls.append(url)

    rules = (Rule(LinkExtractor(allow=(), ), follow=True, callback="parse_item"), )

    def parse_item(self, response):
        item = {}
        # various will follow

        if item:
            yield item

import scrapy
from scrapy_splash import SplashRequest

class WhoscoredSpider(scrapy.Spider):
    name = 'whoscored_spider'
    allowed_domains = ['1xbet.whoscored.com']
    start_urls = ['https://1xbet.whoscored.com/Teams/52/Statistics/Spain-Real-Madrid']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, args={'wait':5})

    def parse(self, response):
        test = response.xpath('//body/div')
        print(test)

from scrapy.spiders import Spider

class TestCCodeSpider(Spider):
    name = 'test_c_code'

    start_urls = ['http://github.com/gouravthakur39/beginners-C-program-examples/blob/master/AllTempScalesConv.c/']

    custom_settings = {'FEED_URI': "test_ c4.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):

        ids = response.xpath("//table[@class='highlight tab-size js-file-line-container']/tr/td/@data-line-number").extract()

        for i in ids:
            yield {
                'extract': response.xpath("string(//td[@id='LC%s'])" % i).extract()
            }
import json


class QuotesScrollSpider(scrapy.Spider):
    name = "quotes-scroll"
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {'author.name': quote['author']['name'], 'text': quote['text'], 'tags': quote['tags']}

        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)

process = CrawlerProcess({
    'FEEDS': {
        'output.csv': {
            'format': 'csv',
            'encoding': 'utf-8-sig',
        }
    }
})
process.crawl(QuotesScrollSpider)
process.start()

#
# process = CrawlerProcess()
# process.crawl(TestCCodeSpider)
# process.start()


