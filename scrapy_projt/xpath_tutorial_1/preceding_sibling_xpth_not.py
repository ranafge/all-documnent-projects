from scrapy.selector import Selector

html ="""<records>
  <born name="Alicex" year="1970"/>
  <born name="Bobx" year="1980"/>
  <died name="Alice" year="2015"/>
</records>"""

data = Selector(text=html)

print(data.xpath('//born[not(@name=//died/@name)]').getall())
print(data.xpath('//died/preceding-sibling::born/@name').getall())
