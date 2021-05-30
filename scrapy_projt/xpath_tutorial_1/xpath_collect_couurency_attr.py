import scrapy

html="""<input type = "hidden" data-currency = "USD" data-sell = "78" data-buy = "74.19">
<input type = "hidden" data-currency = "USD" data-sell = "78" data-buy = "74.19">
<input type = "hidden" data-currency = "USD" data-sell = "78" data-buy = "74.19">"""

data = scrapy.Selector(text=html)

res = data.xpath('string(//*[@*[contains(., "USD")]]/@data-buy)').get()
print(res)
