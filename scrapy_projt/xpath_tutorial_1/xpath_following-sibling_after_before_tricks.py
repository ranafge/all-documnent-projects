import scrapy

html ="""<c>TTTT</c>
<a>AAAA</a>
<b>BBBB</b>
<c>CCCC</c>
<d>DDDD</d>
<c>CCCC</c>"""

data = scrapy.Selector(text=html)
print(data.xpath('//b/following-sibling::*[1][self::c]').get())
