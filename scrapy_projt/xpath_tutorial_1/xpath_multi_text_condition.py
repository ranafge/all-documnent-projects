from scrapy.selector import Selector

html ="""<quotes>
  <category name="Sport">
   <author>James Small<quote date="09/02/1985">Quote One</quote><quote             date="11/02/1925">Quote nine</quote></author>
  </category>
   <category name="Music">
   <author>Stephen Swann
 <quote date="04/08/1972">Quote eleven</quote></author>
  </category>
  </quotes>"""

data = Selector(text=html)

print(data.get())
print('My data:')
# print(data.xpath('string(//quotes/category[@name="Sport"]/author)').get())
# print(data.xpath('string-join(//quotes/category[@name="Sport"]/author/text() ,' ')').get())
# print(data.xpath('concat(//*/author/text()[3], //*/author/text()[2], //*/author/text()[3])').getall())

