from scrapy.selector import Selector

html="""<li class="attribute  ">fs</li>
<li class="attribute">fsd</li>"""

data = Selector(text=html)
# print(data.xpath("//li"))
print(data.xpath("//li[contains(concat(' ', normalize-space(@class),' '), 'attribute  ')]"))
print(data.xpath("//li[normalize-space(@class) = 'attribute']/text()").getall()                                                                                                                                                                                                  )

