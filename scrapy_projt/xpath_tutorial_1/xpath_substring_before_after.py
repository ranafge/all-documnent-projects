import scrapy
html ="""<div class="demo">Prize - 4 G - 14.15</div>"""

data = scrapy.Selector(text=html)
print(data.xpath("substring-before(//div, ' - ')").get())
print(data.xpath("substring-before(substring-after(//div,' - '),' - ')").get())
print(data.xpath("substring-after(substring-after(//div,' - '),' - ')").get())
print(data.xpath("substring-before(//div, '-')").get())
print(data.xpath("substring-after(substring-after(//div, '-'), '-')").get())
print(data.xpath("substring-before(substring-after(//div, '-'), '-')").get())
