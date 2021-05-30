html ="""<tr> 
  <td><input name="Choice" type="radio" value="someValue"></td>
  <td><a href="">text</a></td>
</tr>"""

import scrapy

data = scrapy.Selector(text=html)

print(data.xpath('//td[./a[text()="text"]]/preceding-sibling::td'))
