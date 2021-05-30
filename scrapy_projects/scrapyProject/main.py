
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys


class AtabDSpider(scrapy.Spider):
    name = 'atab_d'

    def start_requests(self):

        yield SeleniumRequest(
            url = "https://www.atab.org.bd/Member/Dhaka_Zone",
            #url = "https://www.bit2lead.com",
            #wait_time = 15,
            wait_time = 3,
            callback = self.parse
        )

    def parse(self, response):
        companies = response.xpath("//ul[@class='row']/li")
        print("Numbers Of Iterable Item: " + str(len(companies)))
        for company in companies:
            yield {
                "company": company.xpath(".//div[@class='card']/div[1]/div/a/h3[@data-bind='text: NameOfOrganization']/text()").get()
                #also tried
                #"company": company.xpath(".//div[@class='card']/div[1]/div/a/h3/text()").get()
            }