import scrapy
from selenium import webdriver
class MovieSpider(scrapy.Spider):
    name = "movies"
    start_urls = ["https://www.thetoptens.com/animals/"]
    def __init__(self):
        self.driver = webdriver.Chrome()
    def parse(self, response):
        self.driver.get(self.start_urls[0])
        print(self.driver.page_source)
        #next_page = self.driver.find_element_by_xpath("//div[@class='pages']/a[@class='g' and text()=9]")
        next_page = self.driver.find_element_by_xpath("//div[@class='pages']/a[text()=2]")
        if next_page:
            next_page.click()
            a = response.xpath("//div[@class='listgrid']/a/text()").getall()
            yield {
                "aaa": a
                 }
        self.driver.close()
