import lxml
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from bs4 import NavigableString

text = """<html>
    <body>
        <div>
            <div class="about-desc about-product-description xs-margin-top">
                <div>
                    <img label="lbl003" alt="alternative" class="" width="70" height="70" src="https://...">
                </div>
            </div>
        </div>
    </body>
</html>
"""
data = Selector(text=text)
print(data.xpath('//div[contains(@class, "about-desc about-product-description")]//img/@label').get())
# print(data.xpath('//td[text()="Samsung"]/preceding-sibling::td/text()').get())
# print(data.response.text)
print()
print()
# print(data.xpath('//bdi[not(parent::del)]/text()').extract())
# soup = BeautifulSoup(text, 'lxml')
# print(soup.prettify())
# rows = soup.find_all('tr')
# for row in rows:
#     fn = row.select('.ndia')
#     for t in fn:
#         print(t.text)

# gettext= soup.find('div', {'class': 'listing-price'}).get_text(strip=True, separator='|').split('|')[0]
# print(soup.select_one('.listing-price').next_element.strip())
# print(gettext)
# print(type(gettext))

# print(data.xpath('//div[@class="zoekres"]').extract_first())


# print(data.xpath("//doc/story[contains(., 'Yahoo')]//text()").getall())
# print(data.xpath("//items/item/interestingAttribute"))
# print(data.xpath("count(//element/Element1[namespace-uri()='mynamespace'])").get())
# print(data.xpath("//div[@class='example']/a[contains(@onclick, 'Test2')]").get()) ok
# print(data.xpath("//div[span[text()='Company name']]/input/@type").get())
# print(data.xpath("count(//section[ancestor::section])").get())
# print(data.xpath("//table//tbody//tr//td//div//input[@data-model-key = //table//thead//span[translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='foo']/parent::th/@data-th-key]/text()").get())
# print(data.xpath("//colors/child::color/child::colorvalue/text()").getall())
# print(data.xpath("//meta[@name='DCSext.job_id']/@content").get())
# print(data.xpath("//production[not(contains(., 'Film'))]/text()").get())
# print(data.xpath("//bla//a[contains(@prop, 'Foo')]"))
# soup = BeautifulSoup(text, 'lxml')
# print(data.xpath("//node3[@foo='bar']"))
# print(data.xpath("//li[text()='LINE ITEM 2']/following::a[text()='Edit']/text()").get())
# print(soup.prettify())
# print(data.xpath('//book//title[1]/@lang').get())
# print(data.xpath("*//title[1][string(.='eng')]/text()").get())
# print(data.xpath("//*/div[@id='prop_sample']/@data-want").get())
# print(data.xpath("//@lang[1]").get())
# print(data.xpath("//*[contains(concat(' ', @class , ' '), 'atag')]").get())
# print(data.xpath("//div[contains(@class, 'atag') and contains(@class, 'btag')]").get())
# print(data.xpath("//*[contains(text(),'xxx')]"))
# print(data.xpath("//node/text()[position()=2]").get())
# print(data.xpath("//node/child::text()[1]").get())
# print(data.xpath("//category[@name='Sport' and ./author/text()[1]='James Small']")[0].get())
# print(data.xpath("//category[@name='Sport' and author/text()[1]='James Small']").get())
# for data in data.xpath("//category[@name='Sport' and ./author/text()[1]='James Small']"):
#     print(data.xpath('//quote/@date').get(), sep='\n')
# print(data.xpath("//*[text()='qwerty']/text()").getall())
# print(data.xpath("//*[text()='qwerty' and not(text()[1])]/text()").get())
# print(data.xpath("//ul[@class='featureList' and ./li[contains(.,'Model')]]").get())
# print(data.xpath("//tr//td[text()='${nbsp}']"))
# print(data.xpath("//div[@id='id-74385' and @class='guest clearfix']"))
# print(data.xpath("//tr[td='Color Digest ']").get())
# print(data.xpath("//tr[td='Color Digest '][2]/td/following-sibling::td[1]/text()").get())
# print(data.xpath("//tr[td='Color Digest '][1]/td[2]/text()").get())

# select node with out attribute

# print(data.xpath("//node[not(@*)]/text()").get())
# print(data.xpath("//myparent//mychild[contains(text(),'foo')]/text()").get())

# print(data.xpath('//tr[.//*[text()="default"]]/td[@class="action-btn-cell"]'))
print(data.xpath('//bdi[not(parent::del)]/text()').extract())


